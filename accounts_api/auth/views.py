from django.forms import model_to_dict
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from api.utils import ExtendedEncoderAllFields
from django.shortcuts import redirect
from django.contrib.auth.models import Group

from poultry.models import Farm, VetShop


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueRequired(Error):
    """Raised when keys do not match"""
    pass

    def __init__(self, salary, message="please add all required fields"):
            self.salary = salary
            self.message = message
            super().__init__(self.message)


def hydrate(body,fields):
    validated_data = {}
    if fields:
        json_data = json.loads(str(body, encoding='utf-8'))
        data_fields = list(json_data.keys())
        if set(fields).issubset(set(data_fields)):
            for key,val in json_data.items():
                validated_data[key]= json_data.get(key,None)
            return {"success":True,"validated_data":validated_data}
        required = ",".join([i for i in fields if i not in data_fields])
        return {"success":False,"message":"These fields are required: "+ required}
    return {"success":True,"validated_data":validated_data}



@csrf_exempt
def create_account(request):
    resp = {}
    fields = [
        "username",
        "password",
        "full_name",
        "user_type"
        ]
    data = hydrate(request.body,fields)
    if data.get("success"):
        validated_data = data.get("validated_data")
        password = validated_data.pop("password")
        # authenticate user
        try:
            user = User.objects.create(**validated_data)
        except Exception as e:
            if "UNIQUE constraint" in str(e):
                resp["success"]=False
                resp["message"]="A user exists with same username"
            else:
                resp["success"]=False
                resp["message"]=str(e)
        else:
            user.set_password(password)
            user.save()
            login(request,user)
            # check permission and redirect accordingly
            # messages.success(request,"Login Successful")
            # is a vet?
            # is a poultry owner?
            # is a normal user?
            resp["success"]=True
            resp["message"]="account created and you're logged in successfully!"
            farm = None
            user_obj = model_to_dict(user)
            user_obj["farm"]=farm
            if user.user_type == "poultry_farmer":
                user.is_staff = True
                user.save()
                my_group = Group.objects.get(name='Farmers') 
                my_group.user_set.add(user)
                my_group.save()
                # does the farmer have a farm obj in the system?
                farm = None
                try:
                    farm = Farm.objects.get(owner=user)
                except Exception:
                    pass
                user_obj["farm"]=farm
            if user.user_type == "vet_officer":
                user.is_staff = True
                user.save()
                my_group = Group.objects.get(name='Vet Officers') 
                my_group.user_set.add(user)
                my_group.save()
                # does the farmer have a farm obj in the system?
                shop = None
                try:
                    shop = VetShop.objects.get(owner=user)
                except Exception:
                    pass
                user_obj["shop"]=shop
            resp["user"]=user_obj
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def login_user(request):
    resp = {}
    fields = [
        "username",
        "password"
        ]
    data = hydrate(request.body,fields)
    if data.get("success"):
        validated_data = data.get("validated_data")
        username = validated_data.get("username")
        password = validated_data.get("password")
        # authenticate user
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            # check permission and redirect accordingly
            # messages.success(request,"Login Successful")
            # is a vet?
            # is a poultry owner?
            # is a normal user?
            resp["success"]=True
            resp["message"]="login successful!"
            user_obj = model_to_dict(user)
            farm = None
            user_obj["farm"]=farm
            if user.user_type == "poultry_farmer":
                # does the farmer have a farm obj in the system?
                try:
                    farm = Farm.objects.get(owner=user)
                except Exception:
                    pass
                user_obj["farm"]=farm
            resp["user"]=user_obj
            shop = None
            user_obj["shop"]=shop
            if user.user_type == "vet_officer":
                # does the farmer have a farm obj in the system?
                try:
                    shop = VetShop.objects.get(owner=user)
                except Exception:
                    pass
                user_obj["shop"]=shop
            resp["user"]=user_obj
        else:
            resp["success"]=False
            resp["message"]="Please check your credential well"
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')