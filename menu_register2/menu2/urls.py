from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
  path('menu/', views.FormView.as_view(),name='menuindex'),
  path('menulist/',views.list_index, name='listindex'),
  path('',views.top_index,name='topindex'),
]