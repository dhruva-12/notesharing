
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    #path('',views.index,name="home"),
    path('', views.index, name="index"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('signup', views.signup, name="signup"),
    path('notes/', views.notesadd, name="notes"),
    path('notesshow/', views.notesshow, name="notesshow"),
    path('notesedit/<int:id>', views.notesedit, name="notesedit"),

    #path('registration/sign_up/',views.sign_up,name="sign-up")
]