from django_tables2 import tables, columns
from .models import UserProfile

class UserTable(tables.Table):
    class Meta:
        model = UserProfile
        template_name = "django_tables2/bootstrap5.html"
        fields = ("email", "first_name", "last_name", "date_joined")
        attrs = {
            'class': 'table table-striped table-hover',
            'thead': {
                'class': 'table-dark'
            }
        }

    email = columns.EmailColumn(linkify=True)
    date_joined = columns.DateTimeColumn(format='d/m/Y H:i')
