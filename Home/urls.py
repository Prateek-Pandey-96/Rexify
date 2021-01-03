from django.urls import path
from Home import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('home/', views.index, name='home'),
    path('', views.index, name='home'),
    path('templates/', views.templates, name='templates'),
    path('contact/', views.contact, name='contact'),
    path('create/<int:pk>/', views.create, name='create'),
    path('viewResume/', views.viewResume, name='viewResume'),
    path('intermediate/', views.intermediate, name='intermediate'),
    path('viewBasic/<int:pk>',views.viewBasic, name="basic-view")
]
