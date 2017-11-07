from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .helpers import send_activation_token, activate_user, accept_previous_logins, send_suspicious_login_message
from .forms import RegisterForm, UserProfileForm, PleioTOTPDeviceForm
from .models import User, PreviousLogins
from django.urls import reverse
from base64 import b32encode
from binascii import unhexlify
from django_otp.util import random_hex
import django_otp
from django.conf import settings


def home(request):
    if request.user.is_authenticated():
        return redirect('profile')

    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated():
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                name=data['name'],
                email=data['email'],
                password=data['password2'],
                accepted_terms=data['accepted_terms'],
                receives_newsletter=data['receives_newsletter']
            )

            send_activation_token(request, user)

            return redirect('register_complete')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def register_complete(request):
    return render(request, 'register_complete.html')


def register_activate(request, activation_key=None):
    if request.user.is_authenticated():
        return redirect('profile')

    user = activate_user(activation_key)

    if user:
        auth.login(request, user)
        return redirect('profile')

    return render(request, 'register_activate.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()

    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


def avatar(request):
    DEFAULT_AVATAR = '/static/images/gebruiker.svg'

    print(request.GET['guid'])
    user = User.objects.get(id=request.GET['guid'])
    print(user.avatar)

    try:
        user = User.objects.get(id=int(request.GET['guid']))
        if user.avatar:
            return redirect('/media/' + str(user.avatar))
    except User.DoesNotExist:
        pass

    return redirect(DEFAULT_AVATAR)


@login_required
def tf_setup(request):
    if request.method == 'POST':
        key = request.session.get('tf_key')
        form = PleioTOTPDeviceForm(data=request.POST, key=key, user=request.user)

        if form.is_valid():
            device = form.save()
            django_otp.login(request, device)
            return redirect('two_factor:setup_complete')

    else:
        key = random_hex(20).decode('ascii')
        rawkey = unhexlify(key.encode('ascii'))
        b32key = b32encode(rawkey).decode('utf-8')

        request.session['tf_key'] = key
        request.session['django_two_factor-qr_secret_key'] = b32key

    return render(request, 'tf_setup.html', {
        'form': PleioTOTPDeviceForm(key=key, user=request.user),
        'QR_URL': reverse('two_factor:qr')
    })


def accept_previous_login(request, acceptation_key=None):
    try:
        accept_previous_logins(request, acceptation_key)
    except:
        pass

    return redirect('profile')

def check_users_previous_logins(request, user, device_id):
    check_previous_logins = settings.CHECK_PREVIOUS_LOGINS
    session = request.session

    result = True

    try:
        login = PreviousLogins.objects.get(device_id=device_id)
        previous_login_present = login.confirmed_login
    except:
        previous_login_present = False

    if previous_login_present:
        #cookie is present so no need to send an email and no further checking is requiered
        check_previous_logins = False
        PreviousLogins.update_previous_login(session, login.pk)

    if check_previous_logins:
        if not user.logged_in_previously(session, device_id):
            #no confirmed matching login found, so email must be sent
            send_suspicious_login_message(request, device_id, user)
            result = False

    return result
