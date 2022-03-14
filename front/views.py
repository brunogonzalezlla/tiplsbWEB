from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from TIPLSB import tiplsb, tip_decode
from PIL import Image

def index(request):
    return render(request, 'base.html')


def check_initialized(request):
    if request.method == 'POST':
        obj = tiplsb(request.FILES['image'])
        response = obj.init
        if obj.init['Line'] == 1:
            response['Initialized'] = False
        else:
            response['Initialized'] = True
        return JsonResponse(response)


def init_and_add(request):
    i = tiplsb(request.FILES['image'], hash = request.POST['hash'], redundancy = request.POST['redundancy'])
    i.add(request.POST['name'], request.POST['platform'])

    array = i.img_array.reshape(i.height, i.width, 3)
    image = Image.fromarray(array.astype('uint8'), 'RGB')

    response = HttpResponse(content_type='image/png')

    image.save(response, "PNG")

    return response


def add(request):
    i = tiplsb(request.FILES['image'])
    i.add(request.POST['name'], request.POST['platform'])

    array = i.img_array.reshape(i.height, i.width, 3)
    image = Image.fromarray(array.astype('uint8'), 'RGB')

    response = HttpResponse(content_type='image/png')

    image.save(response, "PNG")

    return response


def get_path(request):
    original_image = request.FILES['image']
    modified_image = request.FILES['original-image']
    path = tip_decode(modified_image, original_image)

    print(path)
    d = {}

    for e, i in zip(path, range(0, len(path))):
        e_split = e.split("|")
        d[i] = {"Author": e_split[1], "Platform": e_split[2], "Time": e_split[3]}

    return JsonResponse(d)
