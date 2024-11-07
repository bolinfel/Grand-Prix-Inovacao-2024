from django.views.generic import TemplateView

class MonitoramentoView(TemplateView):
    template_name = 'Monitoramento.html'

class AlertasViews(TemplateView):
    template_name = 'Alertas.html'

class AnaliseDadosViews(TemplateView):
    template_name = 'AnaliseDados.html'
