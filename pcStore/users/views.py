from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно! Добро пожаловать.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        print(f"📥 Email: {email} | Пароль: {password}")

        # Прямая проверка логина/пароля
        user = authenticate(request, username=email, password=password)

        if user is not None:
            print(f"✅ Пользователь найден: {user.email}")
            login(request, user)
            print("🚀 Выполняю редирект...")
            return redirect('home')  # Убедись, что в urls.py есть name='home'
        else:
            print("❌ Неверный email или пароль")
            messages.error(request, 'Неверный email или пароль')

    return render(request, 'users/login.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

def user_logout(request):
    logout(request)
    return redirect('home')