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
    path('finalPage/<int:pk>/',views.finalPage , name="finalPage"),
    path('finalPage2/<int:pk>', views.finalPage2, name="finalPage2"),
    path('intermediate/', views.intermediate, name='intermediate'),
    path('viewBasic/<int:pk>',views.viewBasic, name="basic-view"),
    path('viewAvg/<int:pk>',views.viewAvg, name="average-view")
]
