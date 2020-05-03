from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questionId>/', views.getDetails, name='getDetails'),
    path('results/<int:questionId>/', views.getResults, name='getResults'),
    path('vote/<int:questionId>/', views.vote, name='vote'),
]