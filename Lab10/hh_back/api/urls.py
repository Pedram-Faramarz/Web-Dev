from django.urls import path
from . import views
from .views import VacanciesListView

urlpatterns = [
    path('companies/', views.companies_list, name='companies_list'),
    path('companies/<int:id>/', views.companies_detail, name='company_detail'),
    path('companies/<int:id>/vacancies/', views.company_vacancies, name='company_vacancies'),
    path('vacancies/',VacanciesListView.as_view(), name='vacancies_list'),
    path('vacancies/<int:id>/', views.vacancies_detail, name='vacancies_detail'),
    path('vacancies/top_ten/', views.top_ten_vacancies, name='top_ten_vacancies'),
]
