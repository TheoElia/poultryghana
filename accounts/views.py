from django.shortcuts import render,redirect
from poultry.models import Farm, Product, Record, VetShop
from django.contrib import messages

# Create your views here.
def hydrate_request_data(body):

    validated_data = {}
    json_data = body
    for key,val in json_data.items():
        validated_data[key]=val
    validated_data.pop("csrfmiddlewaretoken")
    return validated_data


def index(request):
    args = {}
    template = "landing/index.html"
    args["products"] = Product.objects.all()
    return render(request,template,args)

def login_page(request):
    args = {}
    template = "accounts/login.html"
    return render(request,template,args)


def register(request):
    args = {}
    template = "accounts/register.html"
    return render(request,template,args)


def dashboard(request):
    args = {}
    template = "accounts/dashboard.html"
    return render(request,template,args)


def records(request,pen_no):
    args = {}
    args["record"] = Record.objects.get(pen_no=pen_no)
    template = "accounts/records.html"
    return render(request,template,args)


def add_farm(request):
    args = {}
    if request.method == "POST":
        form_qury = request.POST
        form = hydrate_request_data(form_qury)
        cover_image = request.FILES.get("cover_image")
        form["owner"] = request.user
        try:
            farm = Farm.objects.create(**form)
        except Exception as e:
            messages.error(request,f"{e}")
        else:
            farm.cover_image = cover_image
            farm.save()
            messages.success(request,f"Your farm has been added successfully")
            args["farm"]=farm
    template = "accounts/add-farm.html"
    return render(request,template,args)


def add_shop(request):
    args = {}
    if request.method == "POST":
        form_qury = request.POST
        form = hydrate_request_data(form_qury)
        cover_image = request.FILES.get("cover_image")
        form["owner"] = request.user
        try:
            shop = VetShop.objects.create(**form)
        except Exception as e:
            messages.error(request,f"{e}")
        else:
            shop.cover_image = cover_image
            shop.save()
            messages.success(request,f"Your farm has been added successfully")
            args["shop"]=shop
    template = "accounts/add-shop.html"
    return render(request,template,args)