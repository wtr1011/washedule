from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^template/$', views.hello_template, name='hello_template'),
    url(r'^postnumber/$', views.get_post_query, name='get_post_query'), 
    url(r'^worktime/$', views.get_worktime, name='get_worktime'),
    url(r'^laundryscale/$', views.get_laundryscale, name='get_laundryscale'),
    url(r'^initend/$', views.init_end_page, name='init_end_page'), 
    url(r'^usual/$', views.usual_page, name='usual_page'), 
    url(r'^today/$', views.today_plan, name='today_plan'), 
    url(r'^weekly/$', views.weekly_plan, name='weekly_plan'), 
]