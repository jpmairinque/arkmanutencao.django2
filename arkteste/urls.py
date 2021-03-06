from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from manutencao import views
from manutencao.views import CompanyViewSet, EquipmentViewSet, CompanyEquipmentsViewSet, ChamadoViewSet, EquipmentChamadosViewSet

router = routers.DefaultRouter()

router.register('api/companies', CompanyViewSet, basename="Companies")
router.register('api/equipments', EquipmentViewSet, basename="Equipments")
router.register('api/chamados', ChamadoViewSet, basename="Chamados")

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',include(router.urls)),
    path('api/companies/<int:pk>/equipments/', CompanyEquipmentsViewSet.as_view()),
    path('api/equipments/<int:pk>/chamados/', EquipmentChamadosViewSet.as_view()),
]
