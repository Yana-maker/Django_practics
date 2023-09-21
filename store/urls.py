from django.urls import path
from store.views import StudentListView, StudentDetailView, ContactsCreateView, StudentCreateView, StudentUpdateView, StudentDeleteView
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
]