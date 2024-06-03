from django.urls import path,include
from .views import user_list,upload_file,index


urlpatterns = [
    path('users/', user_list,name='users'),
    path('upload/',upload_file,name='upload_file'),
    path('',index,name='index')

]
