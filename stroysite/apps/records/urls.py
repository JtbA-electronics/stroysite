from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name = 'main'),
	path('record/<int:pk>/', views.record_detail, name='record_detail'),
	path('record/new', views.record_new, name='record_new'),
	path('record/<int:pk>/edit', views.record_edit, name ='record_edit'),
	path('services',views.services, name='services'),
	path('vacancy', views.vacancy, name= 'vacancy'),
	path('contacts', views.contacts, name='contacts'),
	path('documents', views.documents, name= 'documents'),
]