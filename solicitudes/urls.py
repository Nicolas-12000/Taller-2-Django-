from django.urls import path
from .views import (
    SolicitudCreateView,
    SolicitudConfirmacionView,
    SolicitudListView,
    SolicitudDetailView,
    SolicitudUpdateView,
    SolicitudDeleteView,
)

app_name = 'solicitudes'
urlpatterns = [
    path('', SolicitudListView.as_view(), name='solicitud_list'),
    path('crear/', SolicitudCreateView.as_view(), name='solicitud_create'),
    path('confirmacion/', SolicitudConfirmacionView.as_view(), name='confirmacion'),
    path('<int:pk>/', SolicitudDetailView.as_view(), name='solicitud_detail'),
    path('<int:pk>/editar/', SolicitudUpdateView.as_view(), name='solicitud_update'),
    path('<int:pk>/eliminar/', SolicitudDeleteView.as_view(), name='solicitud_delete'),
]