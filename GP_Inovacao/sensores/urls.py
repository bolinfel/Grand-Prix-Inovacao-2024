from django.urls import path
from sensores.views import AlertasViews, AnaliseDadosViews, MonitoramentoView, SensoresView

urlpatterns = [
    path('monitoramento', MonitoramentoView.as_view(), name='monitoramento'),
    path('analiseDados', AnaliseDadosViews.as_view(), name='analiseDados'),
    path('alertas', AlertasViews.as_view(), name='alertas'),
    path('sensores', SensoresView.as_view(), name='sensores'),
]
