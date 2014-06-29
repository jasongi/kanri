from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	# Recursion YOLO
	return render(request, 'dashboard/index.html')