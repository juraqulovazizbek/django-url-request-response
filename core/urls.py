"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import home_view, get_user_by_id_view, get_post_by_title_view, get_product_by_uuid_view, get_sub_news_by_path_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('users/<int:id>', get_user_by_id_view),
    path('posts/<slug:title>', get_post_by_title_view),
    path('products/<uuid:id>', get_product_by_uuid_view),
    path('news/<path:path>', get_sub_news_by_path_view),
]

# path parameter  : /users/{}
# query parameter : /users/?gender=male&age=18
