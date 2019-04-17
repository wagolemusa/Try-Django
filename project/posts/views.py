# from urllib import quote_plus
from urllib.parse import quote_plus  
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
# Create your views here.
from .models import Post
from .forms import PostForms

def post_create(request):
	"""
	Methods creates the Posts
	"""
	form = PostForms(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_obsolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)


def post_list(request):
	""" list items """
	querySet_list = Post.objects.all()
	paginator = Paginator(querySet_list, 3)

	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	context = {
		"query_list": querySet,
		"title":"list"
	}
	return render(request, "post_list.html", context)
	

def post_update(request, id=None):
	"""
	It updates posts
	"""
	instance = get_object_or_404(Post, id=id)
	form = PostForms(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfuly updated")
		return HttpResponseRedirect(instance.get_obsolute_url())
	else:
		messages.error(request, "Not update")
	context = {
	"title": instance.title,
	"instance": instance,
	"form": form,
	}
	return render(request, "post_form.html", context)


def post_delete(request, id=None):
	"""
	 delete Details 
	"""
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfuly Deleted")
	return redirect("posts:list")

