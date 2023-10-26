from django.urls import path
from doctors import views

urlpatterns = [
    path('', views.main),
    path('search/', views.search),
    path('search/details/<int:id>', views.details, name='details'),
    path('create_view/', views.create_view),
    path('all/', views.all),
    path('<int:id>', views.detail_view),
    path('<int:id>/update', views.update_view, name='Update'),
    path('<id>/delete', views.delete_view),
]