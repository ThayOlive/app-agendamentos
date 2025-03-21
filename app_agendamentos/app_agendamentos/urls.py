"""
URL configuration for app_agendamentos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from agendamentos import views
from django.conf.urls.static import static
from app_agendamentos import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.agendamento, name='agendamento'),
    path('treinamento/', views.treinamento, name='treinamento'),
    path('calendario_agendamento/', views.calendario_agendamento, name='calendario_agendamento'),
    path('calendario/agendamentos/', views.obter_agendamentos, name='obter_agendamentos'),  # Para retornar os eventos em formato JSON, se necessário
    path('cadastrar_docente/', views.cadastrar_docente, name='cadastrardocente'),
    path('cliente/', views.clientes, name='clientes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



