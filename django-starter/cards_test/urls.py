from django.urls import path

from . import views

urlpatterns = [
    path('hello_world/', views.hello_world),
    path('greetings/<str:name>/', views.greetings),
    # path('', views.listCards),
    # path('<int:id>/', views.getCard),
    path('', views.CardListView.as_view()),
    path('<int:id>/', views.CardDetailView.as_view()),
]