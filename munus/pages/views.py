from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm
import pandas as pd
import os
import plotly.express as px
from plotly.offline import plot

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            file_path = uploaded_file.file.path
            file_ext = os.path.splitext(file_path)[1].lower()

            try:
                if file_ext == '.csv':
                    # Detectar automaticamente o separador
                    with open(file_path, 'r') as f:
                        first_line = f.readline()
                        sep = ',' if first_line.count(',') > first_line.count(';') else ';'

                    df = pd.read_csv(file_path, sep=sep)
                elif file_ext in ['.xls', '.xlsx']:
                    df = pd.read_excel(file_path)

                if df.empty:
                    raise ValueError("O arquivo está vazio ou não contém dados válidos")

                # Armazenar arquivo na sessão para uso na página Data
                request.session['current_file'] = file_path

                return render(request, 'pages/upload.html', {
                    'form': form,
                    'table_html': df.to_dict('records'),
                    'columns': df.columns.tolist(),
                    'file_name': uploaded_file.file.name,
                    'show_data_button': True
                })

            except Exception as e:
                # Remover arquivo em caso de erro
                uploaded_file.delete()
                form.add_error('file', f'Erro ao processar arquivo: {str(e)}')

    else:
        form = UploadFileForm()

    return render(request, 'pages/upload.html', {'form': form})

def data(request):
    if not request.session.get('current_file'):
        return redirect('upload_file')

    file_path = request.session['current_file']
    file_ext = os.path.splitext(file_path)[1].lower()

    try:
        # Carregar o arquivo
        if file_ext == '.csv':
            with open(file_path, 'r') as f:
                first_line = f.readline()
                sep = ',' if first_line.count(',') > first_line.count(';') else ';'
            df = pd.read_csv(file_path, sep=sep)
        elif file_ext in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)

        if df.empty:
            raise ValueError("O arquivo está vazio ou não contém dados válidos.")

        # Converter colunas de data automaticamente
        for col in df.columns:
            if pd.api.types.is_string_dtype(df[col]):
                try:
                    df[col] = pd.to_datetime(df[col], errors='ignore')
                except:
                    pass

        # Aplicar filtros
        if request.GET:
            for col, value in request.GET.items():
                if value and col in df.columns:
                    if pd.api.types.is_datetime64_any_dtype(df[col]):
                        # Filtros de data
                        if value.startswith('year:'):
                            year = int(value.split(':')[1])
                            df = df[df[col].dt.year == year]
                        elif value.startswith('month:'):
                            month = int(value.split(':')[1])
                            df = df[df[col].dt.month == month]
                        elif value.startswith('range:'):
                            start_date, end_date = value.split(':')[1].split('|')
                            df = df[(df[col] >= pd.to_datetime(start_date)) & 
                                  (df[col] <= pd.to_datetime(end_date))]
                    else:
                        # Filtros categóricos
                        df = df[df[col] == value]

        # Identificar colunas numéricas, categóricas e de data
        numeric_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        categorical_cols = [col for col in df.columns if pd.api.types.is_string_dtype(df[col])]
        date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]

        # Calcular totalizadores para colunas numéricas
        totals = {}
        for col in numeric_cols:
            totals[col] = {
                'sum': df[col].sum(),
                'mean': df[col].mean(),
                'min': df[col].min(),
                'max': df[col].max()
            }

        # Preparar filtros
        filters = {}
        for col in categorical_cols:
            unique_values = df[col].unique().tolist()
            filters[col] = unique_values

        # Preparar filtros de data
        date_filters = {}
        for col in date_cols:
            years = sorted(df[col].dt.year.unique().tolist())
            months = sorted(df[col].dt.month.unique().tolist())
            date_filters[col] = {
                'years': years,
                'months': months
            }

        return render(request, 'pages/data.html', {
            'totals': totals,
            'filters': filters,
            'date_filters': date_filters,
            'columns': df.columns.tolist(),
            'numeric_cols': numeric_cols,
            'categorical_cols': categorical_cols,
            'date_cols': date_cols,
            'filtered_data': df.to_dict('records')
        })

    except Exception as e:
        return render(request, 'pages/error.html', {
            'error': f'Erro ao processar dados: {str(e)}'
        })
