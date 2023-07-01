from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name="overview"),
    path('operations/', views.operations, name="operations"),
    path('operations/add-member/', views.add_member, name="add_member"),
    path('operations/update_members/', views.update_members, name="update_members"),
    path('operations/reset_game/', views.reset_game, name="reset_game"),

]

