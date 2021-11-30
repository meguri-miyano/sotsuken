from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
  path('menu/', views.FormView.as_view(),name='menuindex'),
  path('menulist/',views.MenuListView.as_view(), name='listindex'),
  path('',views.top_index,name='topindex'),
  #path('menu-detail/<int:pk>/',views.MenuDetailView.as_view(),name='detail'),
]
