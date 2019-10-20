from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
from contacts.models import Contact


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid User Name or Password')
            return redirect('login')

    # If clicking on login page then get request will trigger
    return render(request, template_name='accounts/login.html')


def register(request):
    if request.method == "POST":
        # Handle Registration Logic Here
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']

        # Django provides the inbuilt User Model
        # Check if UserName is already registered
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Testing Username is taken')
            return redirect('register')

        elif User.objects.filter(email__icontains=email).exists():
            messages.error(request, 'Email is already registered with us!')
            return redirect('register')
        elif password != confirm_password:
            messages.error(request, "Password doesn't Match!")
            return redirect('register')
        else:
            # Valid User
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            # Login After Registration
            # auth.login(request, user=user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')

            # First redirect to login page and manually login
            user.save()
            messages.success(request, 'Registration Successful..')
            return redirect('login')

    if request.user.is_authenticated:
        messages.error(request, 'Please logout and register')
        return render(request, template_name='accounts/dashboard.html')

    return render(request, template_name='accounts/register.html')


def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': contacts
    }
    return render(request, template_name='accounts/dashboard.html', context=context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are successfully logged out')
        return redirect(to='index')
