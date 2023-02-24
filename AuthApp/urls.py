from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from AuthApp import views


urlpatterns = [
    path('refresh/', TokenRefreshView.as_view()),

    path('user/', views.UserCreateView.as_view()),
    path('user_list/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),

    path('producto/', views.ProductoCreateView.as_view()),
    path('producto_list/', views.ProductoListView.as_view()),
    path('producto/<int:owner>/<int:pk>/', views.ProductoDetailView.as_view()),
    path('producto/update/<int:owner>/<int:pk>/', views.ProductoUpdateView.as_view()),
    path('producto/delete/<int:owner>/<int:pk>/', views.ProductoDetailView.as_view())
]
