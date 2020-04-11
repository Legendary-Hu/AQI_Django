from django.conf.urls import url

from AQI_App import views

"""
路由匹配，urls绑定视图函数
"""


urlpatterns = [
    url(r'^search/',views.search_city),
    url(r'^map/',views.Map_info),
    url(r'^select/',views.select_by_name),
    url(r'^table/',views.TableList),
    url(r'^top20/',views.Top20),
    url(r'^last20/',views.Last20),
    url(r'^overview/',views.Danger_city),
    url(r'^geo/',views.City_geo),
    url(r'^history_data/',views.History_data),
    url(r'^form/',views.Feedback),



]