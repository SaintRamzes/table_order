from django.urls import re_path, path

from reservation.views import ReservedTableListView, ReservationCreateView, TableListView

urlpatterns = [
    path('tables/', TableListView.as_view(), name='tables_list'),
    path('reserved/', ReservedTableListView.as_view(), name='reserved_list'),
    path('reserve/', ReservationCreateView.as_view(), name='reserve_tables'),
]
