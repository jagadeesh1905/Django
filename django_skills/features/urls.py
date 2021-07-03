from django.urls import path
from features import views
urlpatterns = [
    path('$/',views.index,name = 'info'),
]
