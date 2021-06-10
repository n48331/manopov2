from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.details, name='details'),
    path('map/<str:pk>/', views.location, name='location'),
    path("logout", views.logout, name="logout"),
    path("about", views.about, name="about"),

    path('details/add-gaurdian/', views.CreateGaurdian, name='create_gaurdian'),
    path('details/add-member/<int:pk>/',
         views.CreateMember, name='create_member'),
    path('details/update-gaurdian/<int:pk>',
         views.updateGaurdian, name='update_gaurdian'),
    path('details/update-member/<int:pk>/<int:fk>',
         views.updateMember, name='update_member'),
    path('details/delete-gaurdian/<int:pk>/',
         views.deleteGaurdian, name='delete_gaurdian'),
    path('details/delete-member/<int:pk>/',
         views.deleteMember, name='delete_member'),







]
