from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('search/', views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.DetailView.as_view(), name="post_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
