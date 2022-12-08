from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import json
from api.utils import ExtendedEncoderAllFields
from django.db.models import Sum

from poultry.models import Farm, Record, VetShop

from django.shortcuts import render,redirect,HttpResponse
import json


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
def get_poultry_records(request):
    resp = {}
    fields = [
        "farm"
        ]
    data = hydrate(request.body,fields)
    if data.get("success"):
        validated_data = data.get("validated_data")
        # get farm, prefetch records
        farm = Farm.objects.filter(id=int(validated_data.get("farm"))).prefetch_related("record_records")
        
        if farm:
            farm = farm[0] 
        resp["success"]=True
        resp["records"]=[i for i in farm.records.all()]
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_poultry_record_records(request):
    resp = {}
    fields = [
        "record"
        ]
    data = hydrate(request.body,fields)
    if data.get("success"):
        validated_data = data.get("validated_data")
        # get farm, prefetch records
        record = Record.objects.filter(id=int(validated_data.get("record"))).prefetch_related("weekly_records")
        mortality_perc = 0
        production_perc = 0
        avg_egg_prod_morn = 0
        avg_egg_prod_aft = 0
        avg_egg_prod_evn = 0
        if record:
            record = record[0]
            no_of_birds = record.no_of_birds
            if no_of_birds is None:
                no_of_birds = 1
            total_mortality = record.weekly_records.aggregate(total=Sum("mortality")).get("total") or 0
            total_count = record.weekly_records.count()
            if total_count == 0:
                total_count = 1
            mortality_perc = (total_mortality/no_of_birds)*100
            total_egg_prod_morn = record.weekly_records.aggregate(total=Sum("egg_production_morning")).get("total") or 0
            total_egg_prod_aft = record.weekly_records.aggregate(total=Sum("egg_production_afternoon")).get("total") or 0
            total_egg_prod_evn = record.weekly_records.aggregate(total=Sum("egg_production_evening")).get("total") or 0
            avg_egg_prod_morn = total_egg_prod_morn/total_count
            avg_egg_prod_aft = total_egg_prod_aft/total_count
            avg_egg_prod_evn = total_egg_prod_evn/total_count
            
            production_perc = ((total_egg_prod_morn +total_egg_prod_aft +total_egg_prod_evn)/no_of_birds)*100
        summary = {
            "mortality_perc":round(mortality_perc,2),
            "average_egg_production_morning":round(avg_egg_prod_morn,2),
            "average_egg_production_afternoon":round(avg_egg_prod_aft,2),
            "average_egg_production_evening":round(avg_egg_prod_evn,2),
            "production_perc":round(production_perc,2)
        }
        resp["success"]=True
        resp["records"]=[i for i in record.weekly_records.all()]
        resp["summary"]=summary
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_shop_products(request):
    resp = {}
    fields = [
        "shop"
        ]
    data = hydrate(request.body,fields)
    if data.get("success"):
        validated_data = data.get("validated_data")
        # get farm, prefetch records
        shop = VetShop.objects.filter(id=int(validated_data.get("shop"))).prefetch_related("products")
        if shop:
            shop = shop[0]
        resp["success"]=True
        resp["products"]=[i for i in shop.products.all()]
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def search_api(request):
    resp = {}
    fields = [
        "query"
        ]
    data = hydrate(request.body,fields)
    if data.get("success"):
        validated_data = data.get("validated_data")
        query = validated_data.get("query")
        # farms
        farms = Farm.objects.filter(name__icontains=query)
        # vet shops
        shops = VetShop.objects.filter(name__icontains=query)
        resp["results"] = {
            "farms":[i for i in farms],
            "shops":[i for i in shops]
        }
        resp["success"]=True
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')