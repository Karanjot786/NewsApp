from django.urls import path
from news import views
# get_world
urlpatterns = [
    path('', views.shownews, name='shownews'),
    path('business/', views.shownews1, name='shownews1'),
    path('indin/', views.shownews2, name='shownews2'),
    path('sports/', views.shownews3, name='shownews3'),
    path('world/', views.shownews4, name='shownews4'),
]