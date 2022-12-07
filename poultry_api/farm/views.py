from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import json
from api.utils import ExtendedEncoderAllFields
from django.db.models import Sum

from poultry.models import Farm

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
        farm = Farm.objects.filter(id=int(validated_data.get("farm"))).prefetch_related("records")
        average_mortality = 0
        average_egg_production = 0
        avg_egg_prod_morn = 0
        avg_egg_prod_aft = 0
        avg_egg_prod_evn = 0
        if farm:
            farm = farm[0]
            total_mortality = farm.records.aggregate(total=Sum("mortality"))
            total_count = farm.records.count()
            if total_count == 0:
                total_count = 1
            average_mortality = total_mortality.get("total") or 0/total_count
            total_egg_prod_morn = farm.records.aggregate(total=Sum("egg_production_morning")).get("total") or 0
            total_egg_prod_aft = farm.records.aggregate(total=Sum("egg_production_afternoon")).get("total") or 0
            total_egg_prod_evn = farm.records.aggregate(total=Sum("egg_production_evening")).get("total") or 0
            avg_egg_prod_morn = total_egg_prod_morn/total_count
            avg_egg_prod_aft = total_egg_prod_aft/total_count
            avg_egg_prod_evn = total_egg_prod_evn/total_count
            average_egg_production = (total_egg_prod_morn +total_egg_prod_aft +total_egg_prod_evn)/total_count
        summary = {
            "average_mortality":average_mortality,
            "average_egg_production_morning":avg_egg_prod_morn,
            "average_egg_production_afternoon":avg_egg_prod_aft,
            "average_egg_production_evening":avg_egg_prod_evn,
            "average_egg_production":average_egg_production
        }
        resp["success"]=True
        resp["records"]=[i for i in farm.records.all()]
        resp["summary"]=summary
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
        shops = []
        resp["results"] = {
            "farms":[i for i in farms],
            "shops":shops
        }
        resp["success"]=True
    else:
        resp = data
    dump = json.dumps(resp,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')