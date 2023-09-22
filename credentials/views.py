from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        # role = request.POST['role']

        if password == c_password:
            if User.objects.filter(username=username):
                messages.info(request, "username allready exists")
                return redirect('register')

            elif User.objects.filter(email=email):
                messages.info(request, "email allready exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                role = Group.objects.get(name='my_group_name')
                role.user_set.add(user)
                role.save()
                user.save()
                print("user created")
                return redirect('login')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('credentials:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
