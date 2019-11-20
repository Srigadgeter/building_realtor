from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        # check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email id is being used')
                    return redirect('register')
                else:
                    # Registering the user
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )

                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now Logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(request, 'Registration Successful')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out successfully')
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
