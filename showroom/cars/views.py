from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *


def cars_home(request):
    dataset = cars_data.objects.all()

    # Get page number
    page = request.GET.get('page', 1)

    paginator = Paginator(dataset, 3)

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    # items count
    page_obj = paginator.get_page(page)

    template_data = {
        'dataset': pages,
        'page_obj': page_obj
    }
    return render(request, 'cars_home.html', template_data)


def cars_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        maker = request.POST['maker']
        model = request.POST['model']
        color = request.POST['color']
        types = request.POST['types']
        registration_no = request.POST['reg']

        cars_data.objects.create(name=name, maker=maker, model=model, color=color,
                                 registration_no=registration_no, types=types)
        return redirect('cars_home')
    else:
        return HttpResponse("Bad Request !")


def cars_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        maker = request.POST['maker']
        model = request.POST['model']
        color = request.POST['color']
        registration_no = request.POST['reg']
        types = request.POST['types']

        cars_data.objects.filter(id=id).update(name=name, maker=maker, model=model, color=color,
                                               registration_no=registration_no, types=types)
        return redirect('cars_home')
    else:
        return HttpResponse("Bad Request !")


def cars_del(request, car_id):
    cars_data.objects.get(id=car_id).delete()
    return redirect('cars_home')


def category_filter(request):
    if request.method == 'POST':
        maker = request.POST['maker']
        model = request.POST['model']
        color = request.POST['color']
        types = request.POST['types']

        dataset = cars_data.objects.filter(maker=maker, model=model, color=color, types=types)

        return render(request, 'cars_home.html', {'dataset': dataset})
    else:
        return HttpResponse("Bad Request !")



@api_view(['POST', 'GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_cars_data(request):
    dataset = cars_data.objects.all()
    data_list = list()
    for data in dataset:
        data = model_to_dict(data)
        data_list.append(data)
    return JsonResponse(data_list, safe=False)
