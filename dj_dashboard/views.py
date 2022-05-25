from django.shortcuts import render
from django.http import JsonResponse
from dj_dashboard.models import Order
from django.core import serializers

# Directs user to the specified template.
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

# Sends response with the data
def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

