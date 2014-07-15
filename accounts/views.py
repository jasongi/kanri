from django.shortcuts import render, redirect
from forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission

# Create your views here.
def login(request):
    # check if user has logged in
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            print "Logging in!"
            return redirect("home")
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

def admin(request):
    add_management_form = UserSelectionForm()
    remove_management_form = ManagementSelectionForm()
    change_password_form = ChangePasswordForm()
    return render(request, 'accounts/admin.html', {
        'add_management_form': add_management_form,
        'remove_management_form': remove_management_form,
        'password_form': change_password_form,
        })

def sync(request):
    #for p in Permission.objects.all():
    #   print p

    sync = [
        {
            'group': 'Management',
            'permissions': [
                'add_attendance',
                'read_attendance',
                'change_attendance',
                'delete_attendance',
        
                'add_mentor',
                'read_mentor',
                'change_mentor',
                'delete_mentor',
        
                'add_role',
                'read_role',
                'change_role',
                'delete_role',
        
                'add_ninja',
                'read_ninja',
                'change_ninja',
                'delete_ninja',
        
                'add_dojoterm',
                'read_dojoterm',
                'change_dojoterm',
                'delete_dojoterm',
        
                'add_dojosession',
                'read_dojosession',
                'change_dojosession',
                'delete_dojosession',
        
                'add_shift',
                'read_shift',
                'change_shift',
                'delete_shift',
        
                'add_room',
                'read_room',
                'change_room',
                'delete_room',

                'see_admin',
                'change_user_passowrd',
                'add_management',
                'remove_management',
                'sync_permissions'
            ]
        },
        {
            'group': 'Mentors',
            'permissions': [
                'add_attendance',
                'read_attendance',
                'change_attendance',
                'delete_attendance',
        
                'read_shift',

                'read_dojoterm',
                'read_dojosession',

                'read_room',

                'read_job',
                'register_for_job',

                'view_mentor_dashboard',
            ]
        }
    ]
    

    for s in sync:
        group = Group.objects.get_or_create(name = s['group'])[0]
        group.permissions.clear()
        for permission in s['permissions']:
            perm = Permission.objects.get(codename = permission)
            group.permissions.add(perm)
            print "Added %s to %s" % (perm, group)
        group.save()

    return redirect('accounts:admin')
    
def management_add(request):
    if request.method == 'POST':
        form = UserSelectionForm(request.POST)
        if form.is_valid():
            group = Group.objects.get_or_create(name = 'Management')[0]
            form.cleaned_data['user'].groups.add(group)
            return redirect('accounts:admin')
    else:
        return redirect('accounts:admin')

def management_remove(request):
    if request.method == 'POST':
        form = ManagementSelectionForm(request.POST)
        if form.is_valid():
            group = Group.objects.get_or_create(name = 'Management')[0]
            group.user_set.remove(form.cleaned_data['user'])
            return redirect('accounts:admin')
    else:
        return redirect('accounts:admin')

def change_password_admin(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['user']
            u.set_password(form.cleaned_data['password'])
            u.save()
            return redirect('accounts:admin')
    else:
        return redirect('accounts:admin')

def cp(request):
    return redirect('dashboard:index')