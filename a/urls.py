from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:target>/<str:responder>', views.redirection, name='redirection'),
]

