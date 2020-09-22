"""dev_aleksan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('category/<str:slug>/', get_category, name='category'),
    # path('post-detail/<str:slug>/', post_detail, name='post_detail'),
    path('post/<str:slug>/', BlogPostView.as_view(), name='post'),

]
