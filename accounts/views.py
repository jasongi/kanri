from django.shortcuts import render, redirect
from forms import LoginForm, UserSelectionForm, ManagementSelectionForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
def login(request):
	# check if user has logged in
	if request.user.is_authenticated():
		return redirect('dashboard')

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			auth_login(request, form.user)
			print "Logging in!"
			return redirect("dashboard")
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

def permissions(request):
	add_management_form = UserSelectionForm()
	remove_management_form = ManagementSelectionForm()
	return render(request, 'accounts/permissions.html', {
		'add_management_form': add_management_form,
		'remove_management_form': remove_management_form,
		})

def management_add(request):
	if request.method == 'POST':
		form = UserSelectionForm(request.POST)
		if form.is_valid():
			group = Group.objects.get_or_create(name = 'Management')[0]
			form.cleaned_data['user'].groups.add(group)
			return redirect('accounts:permissions')
	else:
		return redirect('accounts:permissions')

def management_remove(request):
	if request.method == 'POST':
		form = ManagementSelectionForm(request.POST)
		if form.is_valid():
			group = Group.objects.get_or_create(name = 'Management')[0]
			group.user_set.remove(form.cleaned_data['user'])
			return redirect('accounts:permissions')
	else:
		return redirect('accounts:permissions')

def cp(request):
	return redirect('dashboard:index')