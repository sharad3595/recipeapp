from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.recipes),
    path('delete-recipe/<id>',views.recipe_delete),
    path('edit-recipe/<int:pk>',views.recipe_edit),
]

#making media file accessable 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)