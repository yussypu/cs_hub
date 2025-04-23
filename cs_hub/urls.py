"""
URL configuration for cs_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'), 
    path('matrix/', views.course_matrix, name='course_matrix'),
    path('courses/', views.index, name='home'),
    path('year/<int:year>/period/<int:period>/', views.period_view, name='period'),
    path('period/5/logic-notes/', views.logic_notes, name='logic_notes'),
    path('period/5/databases-notes/', views.databases_notes, name='databases_notes'),
    path('period/5/databases/introduction/', views.databases_intro, name='databases_intro'),
    path('info-management/notes/', views.info_management_notes, name='info_management_notes'),
    path("info-management/information-systems/", views.info_management_information_systems, name="info_management_information_systems"),

]
