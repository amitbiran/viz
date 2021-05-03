from django.urls import path
from . import views
urlpatterns = [
    path('health', views.health),
    path('get-all',views.get_all_scans),
    path('get-user-scans', views.get_scans_by_uid),
    path('get-transfers',views.get_transfers),
    path('get-transfers-query',views.get_transfers_query)
]