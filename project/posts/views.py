from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
from .models import Post

def post_create(request):
	return 	HttpResponse("<h1>Create</h1>")

def post_detail(request):
	""" Retrieve """
	return HttpResponse("<h1>Details</h1>")


def post_list(request):
	""" list items """
	querySet = Post.objects.all()

	context = {
		"query_list": querySet,
		"title":"list"
	}
	# if request.user.is_authenticated:
	# 	context = {
	# 		"title":"User's list test concatenate"
	# 	}
	# else:
	# 	context = {
	# 		"title":"list"
	# 	}
	return render(request, "index.html", context)
	# return HttpResponse("<h1>List</h1>")
	

def post_update(request):
	""" update details """
	return HttpResponse("<h1>Update</h1>")


def post_delete(reqest):
	""" delete Details """
	return HttpResponse("<h1>Delete</h1>")


