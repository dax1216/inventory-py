from django.shortcuts import  render, redirect
from inventory.forms import NewUserForm, UpdateUserForm, UpdateProfileForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="inventory/user/login.html", context={"login_form":form})



def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/login")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")

		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "inventory/user/register.html", context={"register_form":form})


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "inventory/user/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')

					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset/done/")

	password_reset_form = PasswordResetForm()

	return render(request=request, template_name="inventory/user/reset_password.html", context={"password_reset_form":password_reset_form})


@login_required
def profile(request):

	if request.method == 'POST':
		if request.POST.get('password_change') is not None:
			password_form = SetPasswordForm(request.user, request.POST)

			if password_form.is_valid():
				password_form.save()
				messages.success(request, "Your password has been changed")

				return redirect('/login')
			else:
				for error in list(password_form.errors.values()):
					messages.error(request, error)
				return redirect('/profile#change-password')
		else:
			user_form = UpdateUserForm(request.POST, instance=request.user)
			profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
			password_form = SetPasswordForm(request.user)

			if user_form.is_valid() and profile_form.is_valid():
				user_form.save()
				profile_form.save()
				messages.success(request, 'Your profile is updated successfully')

				return redirect(reverse('profile'))
	else:
		user_form = UpdateUserForm(instance=request.user)
		profile_form = UpdateProfileForm(instance=request.user.profile)
		password_form = SetPasswordForm(request.user)

	context = {
		'title': 'My Profile',
        'user_form': user_form,
		'profile_form': profile_form,
		'password_form': password_form
	}

	return render(request, 'inventory/user/profile.html', context)




