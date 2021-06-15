from django.urls import path, include
from . import views
from random import randint, choice


app_name = 'reviews'
urlpatterns = [
    path('',views.index_view,name='index_view'),
    path('dept/<str:dept_id>', views.mat_list, name='mat_list'),
    path('mat/<str:mat_id>', views.course_list, name='course_list'),
    path('mat/<str:mat_id>/<str:course_id>', views.course_detail, name = 'course_detail'),
    path('mat/<str:mat_id>/<str:course_id>/add_recom',views.add_recom, name = 'add_recom'),
    path('contacto/',views.contacto,name='contacto'),
    path('msg_send/',views.send_msg,name='sent'),
    path('delete_rev/<str:rev_id>/',views.del_rev,name='del_rev'),
    path('flag_rev/<str:rev_id>',views.flag_rev,name='flag_rev'),
    path('search/',views.search,name='search')
]
