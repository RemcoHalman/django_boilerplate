from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .views import (
                Home, Blog,
                Profile, Project,
                PageDetailView
                )
from . import views

urlpatterns = [
    path('', Home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    ## All pages Automated
    path('<slug>/', PageDetailView.as_view(), name='Page-detailview'),
    ## Special pages
    path('web/blog/', views.Blog, name='blogposts'),
    path('web/projects/', views.Project_items, name='projects'),
    path('accounts/profile/', views.Profile, name='account_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
