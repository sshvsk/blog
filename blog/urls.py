"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from posts.views import index, add_posts
from profiles.views import index_profiles, register, login_view, logout_view
from shop.views import products

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', index, name='index'),
   path('index_profiles/', index_profiles, name='index_profiles'),
   path('register/', register, name='register'),
   path('products/', products, name='products'),
   path('add_posts/', add_posts, name='add_posts'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path("api/", include("api.urls", namespace="api")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
