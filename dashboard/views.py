from django.shortcuts import render, redirect

def index(request):
	# Recursion YOLO
	return redirect('mentors:dashboard')