from django.urls import path
from module_one import views


app_name = 'module_one'

urlpatterns = [
    path('relative/', views.relative_url_templates, name='relative'),
    path('other/', views.other, name='other'),
]
