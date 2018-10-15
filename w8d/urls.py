from django.urls import path

from a import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:responder>', views.default_redirection, name='default_redirection'),
]

