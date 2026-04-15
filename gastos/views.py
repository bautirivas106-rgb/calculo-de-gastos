from django.shortcuts import render
from .models import Gasto # Solo Gasto de acá
from ingresos.models import Ingreso # <--- Traemos Ingreso desde la nueva app

def lista_gastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    ingresos = Ingreso.objects.all().order_by('-fecha')

    total_gastos = sum(g.monto for g in gastos)
    total_ingresos = sum(i.monto for i in ingresos)
    balance = total_ingresos - total_gastos

    context = {
        'gastos': gastos,
        'ingresos': ingresos,
        'total_gastos': total_gastos,
        'total_ingresos': total_ingresos,
        'balance': balance,
    }
    return render(request, 'gastos/lista.html', context)