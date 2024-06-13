from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nova_tema/', views.nova_tema, name="nova_tema"),
    path('ucitel/<int:pk>', views.ucitel, name="ucitel"),
    path('student/<int:pk>', views.student, name="student"),
    path('tema/<int:pk>', views.tema, name="tema"),
    path('statistiky', views.statistiky, name="statistiky"),
    path('update_konzultacie/', views.update_konzultacie, name="update_konzultacie")
]
