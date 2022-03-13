from django.urls import path

from . import views

urlpatterns = [
    path('', views.CardList.as_view()),
    path('<int:id>/', views.CardDetail.as_view()),
]