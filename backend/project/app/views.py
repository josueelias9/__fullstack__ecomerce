from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt


from .models import Product

@csrf_exempt
def index(request):
    # https://docs.djangoproject.com/en/4.2/ref/models/querysets/#values
    a = Product.objects.values()
    if request.method == "GET":
        return JsonResponse(list(a),safe=False)
    if request.method == "POST":
        return JsonResponse({"info":"esto es un post"})
