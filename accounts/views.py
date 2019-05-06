from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
  if request.method == 'POST':
    # Register User
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'This username is taken')
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        messages.error(request, 'This email is being used')
        return redirect('register')
      else:
        # Looks good
        print('Looks good')
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        # # Login after register
        # auth.login(request, user)
        # messages.success(request, 'You are now logged in')
        # return redirect('index')
        user.save()
        messages.success(request, 'You are now registered and can login')
        return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    # Login User
    messages.error(request, 'Testing error message')
    return redirect('login')
  return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')