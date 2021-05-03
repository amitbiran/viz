from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models
from django.core import serializers
import json

# Create your views here.
def health(req):
    return HttpResponse('ok')

def get_all_scans(req):
    scans = models.Scan.objects.all()
    json_scans = serializers.serialize('json',scans)
    return JsonResponse(data= json.loads(json_scans), safe= False)

def check_if_has_user(records,uid):
    for record in records:
        if record.uid == uid:
            return True
    return False

def get_transfers(req):
    result = []
    hospitalId1 = req.GET.get('h1')
    hospitalId2 = req.GET.get('h2')
    hospitalId1_records = models.Scan.objects.filter(hospitalId=hospitalId1)
    hospitalId2_records = models.Scan.objects.filter(hospitalId=hospitalId2)
    for record in hospitalId1_records:
        if check_if_has_user(hospitalId2_records,record.uid):
            result.append(record.uid)
    return JsonResponse(data=result,safe=False)

def get_transfers_query(req):
    hospitalId1 = req.GET.get('h1')
    hospitalId2 = req.GET.get('h2')
    users = models.Scan.objects.raw("""
                                      select a.uid
                                      from ct_scans_scan  a
                                      inner join ct_scans_scan  b 
                                      on a.uid = b.uid
                                      where a.hospitalId = '{}'
                                      and b.hospitalId = '{}'""".format(hospitalId1,hospitalId2))
    json_users = serializers.serialize('json',users)
    return JsonResponse(data=json_users,safe=False)

def get_scans_by_uid(req):
    uid = req.GET.get('uid')
    scans = models.Scan.objects.filter(uid=uid)
    json_scans = serializers.serialize('json',scans)
    return JsonResponse(data=json.loads(json_scans),safe=False)

def write_scan(uid,hospitalId):
    scan = models.Scan(uid = uid, hospitalId = hospitalId)
    scan.save()



