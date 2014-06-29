from django.shortcuts import render, redirect
from forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	# check if user has logged in
	if request.user.is_authenticated:
		return redirect('dashboard:index')

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			auth_login(request, form.user)
			print "Logging in!"
			return redirect("dashboard:index")
	else:
		form = LoginForm()
	return render(request, 'accounts/login.html', {
		'form': form
		})

@login_required
def logout(request):
	if request.method == "POST":
		auth_logout(request)
		return redirect('dashboard:index')
	return render(request, 'accounts/logout.html')

def cp(request):
	return redirect('dashboard:index')