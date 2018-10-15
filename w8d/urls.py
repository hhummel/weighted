from django.urls import path

from a import views

urlpatterns = [
    path('', views.default_redirection, name='default_redirection'),
    path('<str:responder>', views.responder_redirection, name='responder_redirection'),
]

