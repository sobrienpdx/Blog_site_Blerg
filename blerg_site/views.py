from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.clean_password2()
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				group = Group.objects.get(name='Commenters')
				user.groups.add(group) #documentation in code guild under user management
			return redirect('blerg_app:index')
		else:
			return HttpResponse('Invalid form')
	context = {'form': UserCreationForm()}
	return render(request, 'registration/register.html', context)
