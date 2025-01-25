from pages.models import UserProfile
import random
import string

def generate_unique_email(base_email):
    """Gera um email único adicionando um sufixo numérico"""
    counter = 1
    while True:
        unique_email = f"{base_email.split('@')[0]}_{counter}@{base_email.split('@')[1]}"
        if not UserProfile.objects.filter(email=unique_email).exists():
            return unique_email
        counter += 1

def generate_password(length=12):
    """Gera uma senha aleatória"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Dados base para usuários de teste
base_users = [
    {
        "base_email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "is_staff": True,
        "is_superuser": True,
    },
    {
        "base_email": "user@example.com",
        "first_name": "Regular",
        "last_name": "User",
    },
]

# Cria 5 usuários de teste
for i in range(5):
    base_data = base_users[i % len(base_users)]
    try:
        password = generate_password()
        user = UserProfile.objects.create_user(
            email=generate_unique_email(base_data["base_email"]),
            password=password,
            first_name=f"{base_data['first_name']} {i+1}",
            last_name=base_data["last_name"],
            is_staff=base_data.get("is_staff", False),
            is_superuser=base_data.get("is_superuser", False),
            role='usuario'  # Definindo um valor padrão para o campo role
        )
        
        print(f"Usuário criado: {user.email} (Senha: {password})")
        
    except Exception as e:
        print(f"Erro ao criar usuário: {str(e)}")
        continue

print("Processo de criação de usuários de teste concluído!")
