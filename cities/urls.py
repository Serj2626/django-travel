from django.urls import path
from cities import views

app_name = 'cities'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.CityListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='delete'),
    path('add', views.CityCreateView.as_view(), name='create'),
]
