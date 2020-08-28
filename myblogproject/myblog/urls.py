from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create10/', views.create10, name='create10'),
    path('new/', views.new, name="new"),
    path('<int:post_id>/', views.detail, name="detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)