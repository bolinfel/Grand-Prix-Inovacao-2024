from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Sensor, Leituras
from django.utils import timezone
import random
from django.http import JsonResponse
import json

class MonitoramentoView(TemplateView):
    template_name = 'Monitoramento.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensores'] = Sensor.objects.all()

        # Obter a última leitura de cada sensor
        ultimas_leituras = {}
        for sensor in context['sensores']:
            ultima_leitura = Leituras.objects.filter(FK_Sensor=sensor).order_by('-Data').first()
            if ultima_leitura:
                ultimas_leituras[sensor.id] = {
                    'sensor': sensor,
                    'valorA': ultima_leitura.ValorA,
                    'valorB': ultima_leitura.ValorB,
                    'data': ultima_leitura.Data
                }

        context['ultimas_leituras'] = ultimas_leituras
        return context

    def post(self, request, *args, **kwargs):
        try:
            # Carrega o corpo JSON da requisição
            data = json.loads(request.body)
            sensor_id = data.get('sensor_id')
            
            # Validação do sensor_id
            if not sensor_id:
                return JsonResponse({'error': 'ID do sensor não fornecido.'}, status=400)

            # Busca o sensor ou retorna erro se não encontrado
            sensor = Sensor.objects.get(id=sensor_id)
            leituras = Leituras.objects.filter(FK_Sensor=sensor).order_by('Data')

            # Formata os dados para o gráfico
            valoresA = [leitura.ValorA for leitura in leituras]
            valoresB = [leitura.ValorB for leitura in leituras]
            datas = [leitura.Data.strftime('%Y-%m-%d %H:%M') for leitura in leituras]

            return JsonResponse({
                'sensor_name': str(sensor),
                'valoresA': valoresA,
                'valoresB': valoresB,
                'datas': datas
            })
        
        except Sensor.DoesNotExist:
            return JsonResponse({'error': 'Sensor não encontrado.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Erro no formato JSON da requisição.'}, status=400)





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

