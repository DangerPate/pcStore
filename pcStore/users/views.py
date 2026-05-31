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
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '').strip()
        phone = request.POST.get('phone', '').strip()

        if not nickname:
            messages.error(request, 'Никнейм не может быть пустым.')
        else:
            request.user.nickname = nickname
            request.user.phone = phone

            if 'avatar' in request.FILES:
                request.user.avatar = request.FILES['avatar']

            request.user.save()
            messages.success(request, 'Профиль успешно обновлён!')
            return redirect('users:profile')

    # 🔥 Передаём счётчики для меню (если используются)
    from cart.models import CartItem, Favorite
    fav_count = Favorite.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    cart_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0

    return render(request, 'users/profile.html', {
        'user': request.user,
        'fav_count': fav_count,
        'cart_count': cart_count,
    })

def user_logout(request):
    logout(request)
    return redirect('home')