import datetime
import base64

from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *
@login_required
def index(request):
	if request.method == 'GET':
		return render(request, 'index.html', {
			'user':request.user,
			})


@login_required
def profile(request):
	if request.method == 'GET':
		form = UserForm(instance=request.user)
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	return render(request, 'profile.html', {
		'form' : form
		})

def signup(request):
	if request.method == 'GET':
		userForm = UserCreationForm()
		return render(request, 'signup.html', {'form' : userForm})
	if request.method == 'POST':
		userForm = UserCreationForm(request.POST)
		try:
			user = userForm.save()
		except ValueError as e:
			return render(request, 'signup.html', {'form' : userForm})
		return redirect(index)