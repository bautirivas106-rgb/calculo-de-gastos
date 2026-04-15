from django.shortcuts import render
from .models import Gasto, Ingreso # Importamos ambos

def lista_gastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    ingresos = Ingreso.objects.all().order_by('-fecha')
    
    total_gastos = sum(g.monto for g in gastos)
    total_ingresos = sum(i.monto for i in ingresos)
    balance = total_ingresos - total_gastos
    
    return render(request, 'gastos/lista.html', {
        'gastos': gastos,
        'ingresos': ingresos,
        'total_gastos': total_gastos,
        'total_ingresos': total_ingresos,
        'balance': balance
    })