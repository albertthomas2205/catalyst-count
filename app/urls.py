from django.urls import path,include
from .views import user_list,upload_file


urlpatterns = [
    path('users/', user_list,name='users'),
    path('upload/',upload_file,name='upload_file'),

]
