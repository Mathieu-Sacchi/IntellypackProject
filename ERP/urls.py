from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('creer_dossier/', views.create_dossier, name="creer_dossier"),
    path('update_dossier/<str:dossier_id>/', views.update_dossier, name="update_dossier"),
    path('supprimer_dossier/<str:dossier_id>/', views.delete_dossier, name="supprimer_dossier"),
    path('pdf/<str:dossier_id>/', views.get_pdf, name="pdf"),
]
