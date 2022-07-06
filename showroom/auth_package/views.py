from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random as rd
import string


# send mail function
def send_pass_email(email, random_password):
    send_mail(
        'Welcome Note',
        f'Hi User , Welcome to Showroom , this is your system generated password ==> {random_password}.',
        'showroom.com',
        [email],
        fail_silently=False,
    )


# signup function
def signup_form(request):
    if request.user.is_authenticated:
        return redirect('cars_home')
    else:
        if request.POST:
            username = request.POST['username']
            email = request.POST['email']

            # random password generation
            random_password = ''.join(rd.choice(string.ascii_letters).lower() for i in range(8))
            # registering user
            user = User.objects.create_user(username=username, email=email, password=random_password, is_staff=True)
            # adding to specific group
            group = Group.objects.get(name='basic')
            # sending email with random generated password
            send_pass_email(email, random_password)
            user.groups.add(group)
            return redirect('login')
        return render(request, 'signup.html')
