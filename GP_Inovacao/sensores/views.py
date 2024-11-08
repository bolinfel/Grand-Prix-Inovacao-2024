from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Sensor, Leituras
from django.utils import timezone
import random

class MonitoramentoView(TemplateView):
    template_name = 'Monitoramento.html'

class AlertasViews(ListView):
    model = Leituras
    template_name = 'Alertas.html'
    context_object_name = 'leituras'
    ordering = ['-Data']  # Ordena as leituras pela data mais recente


class AnaliseDadosViews(TemplateView):
    template_name = 'AnaliseDados.html'

class SensoresView(TemplateView):
    template_name = 'Sensores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensores'] = Sensor.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        sensor_id = request.POST.get('sensor_id')
        valorA = random.uniform(0, 100)  # Exemplo de valor aleatório para simulação
        valorB = random.uniform(0, 100)  # Exemplo de valor aleatório para simulação
        data = timezone.now()

        if sensor_id:
            sensor = Sensor.objects.get(id=sensor_id)
            Leituras.objects.create(FK_Sensor=sensor, ValorA=valorA, ValorB=valorB, Data=data)
            return redirect('alertas')

        return self.get(request, *args, **kwargs)

