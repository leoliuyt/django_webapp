from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.showBlogList, name='showBlogList'),
    path(r'(\d+)$', views.showBlog, name='showBlog'),
]