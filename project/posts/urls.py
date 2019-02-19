from django.urls import path

from django.conf.urls import  url
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

app_name = 'posts'
urlpatterns = [

  path('',  post_list),
  path('create/', post_create),
  path('<int:id>/',post_detail, name='detail'),
  path('update/', post_update),
  path('delete/', post_delete),
]