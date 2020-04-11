import random
import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
from django.core import serializers
from django.shortcuts import render


# Create your views here.
from django.template import loader

from AQI_App.models import City_info, City_local, Aqi_data, city_geocode, data_history


# 模糊搜索
def search_city(request):
    if request.method =="GET":
        search_word = request.GET.get('cityname') #获取get参数
        city_list = City_info.objects.filter(city_name__contains=search_word).only('city_name') #过滤查询包含关键字的数据
         # print(city_list)
        city_name = [item.city_name for item in city_list] #提取cityname字段
        return HttpResponse(json.dumps(city_name,ensure_ascii=False),content_type="application/json,charset=utf-8") #返回json数据
        # return JsonResponse({
        #     "cityname":city_name
        # })
    else:
        return JsonResponse({
            "status":0,
            "message": "You need GET method"
        })
def Map_info(request):

    city_list = City_info.objects.values("city_name","aqi","datetime")
    data = {}
    data = list(city_list)

    # return JsonResponse(data,safe=False)
    return HttpResponse(json.dumps(data, ensure_ascii=False,cls=CJsonEncoder), content_type="application/json,charset=utf-8")


def select_by_name(request):
   if request.method == 'POST':
       cityname = request.POST.get("cityname")
       # print(cityname)
       # city_list = request.POST.getlist("cityname")
       info = City_info.objects.get(city_name=cityname)
       num = City_info.objects.filter(aqi__lt=info.aqi).exclude(aqi=0).count() #获取排名
       rand = num +1
       # print(rand)
       data = Aqi_data.objects.get(city_name=cityname)


       return JsonResponse({
           "status":1,
           "data": {
               'cityname':cityname,
               'aqi':info.aqi,
               'level_index':info.level_index,
               'pm25':data.pm25,
               'pm10':data.pm10,
               'SO2':data.so2,
               'NO2':data.no2,
               'CO' :data.co,
               'O3' :data.o3,
               'rand':rand,
               'datetime':info.datetime
           }
       })


def TableList(request):
    city_list = City_info.objects.all()
    data = []
    for item in city_list: #利用django 的model_to_dict将queryset序列化成字典
        item_dict = model_to_dict(item)
        data.append(item_dict)
    return HttpResponse(json.dumps(data, ensure_ascii=False,cls=CJsonEncoder), content_type="application/json,charset=utf-8")

# 空气质量top20城市
def Top20(request):
    # key_word = request.GET.get("keyword")
    top20 = City_info.objects.all().exclude(aqi=0).order_by('aqi')[:20]
    # print(top20)
    data = []
    for item in top20:
        item_dict = model_to_dict(item)
        data.append(item_dict)
    return HttpResponse(json.dumps(data,ensure_ascii=False,cls=CJsonEncoder),content_type="application/json,charset-utf-8")


def Last20(request):
    last20 = City_info.objects.all().order_by('-aqi')[:20]
    data = []
    for item in last20:
        item_dict = model_to_dict(item)
        data.append(item_dict)
    return HttpResponse(json.dumps(data, ensure_ascii=False, cls=CJsonEncoder),content_type="application/json,charset-utf-8")

def Danger_city(request):
    serious = City_info.objects.filter(level_index='严重污染').count()
    danger = City_info.objects.filter(level_index='重度污染').count()
    mid_poll = City_info.objects.filter(level_index='中度污染').count()
    light_poll = City_info.objects.filter(level_index='轻度污染').count()
    mid_class = City_info.objects.filter(level_index='良').count()
    top_class = City_info.objects.filter(level_index='优').count()
    return JsonResponse({
            "serious": serious,
            "danger": danger,
            "mid_poll": mid_poll,
            "light_poll": light_poll,
            "mid_class": mid_class,
            "top_class": top_class,
    })
def City_geo(request):
    city_name = request.GET.get("cityname")
    if(city_name == '甘南州'):
        city_name = '甘南藏族自治州'
    if (city_name == '大理州'):
        city_name = '大理白族自治州'
    if (city_name == '德宏州'):
        city_name = '德宏傣族景颇族自治州'
    if (city_name == '甘孜州'):
        city_name = '甘孜藏族自治州'
    if (city_name == '凉山州'):
        city_name = '凉山彝族自治州'
    if (city_name == '楚雄州'):
        city_name = '楚雄彝族自治州'
    if (city_name == '怒江州'):
        city_name = '怒江傈僳族自治州'
    if (city_name == '迪庆州'):
        city_name = '迪庆藏族自治州'
    if (city_name == '海北州'):
        city_name = '海北藏族自治州'
    if (city_name == '恩施州'):
        city_name = '恩施土家族苗族自治州'
    if (city_name == '果洛州'):
        city_name = '果洛藏族自治州'
    if (city_name == '海南州'):
        city_name = '黄南藏族自治州'
    if (city_name == '海西州'):
        city_name = '海西蒙古族藏族自治州'
    if (city_name == '红河州'):
        city_name = '红河哈尼族彝族自治州'
    if (city_name == '文山州'):
        city_name = '文山壮族苗族自治州'
    if (city_name == '黔东南州'):
        city_name = '黔东南苗族侗族自治州'
    if (city_name == '黄南州'):
        city_name = '黄南藏族自治州'
    if (city_name == '临夏州'):
        city_name = '临夏回族自治州'
    if (city_name == '黔南州'):
        city_name = '黔南布依族苗族自治州'
    if (city_name == '黔西南州'):
        city_name = '黔西南布依族苗族自治州'
    if (city_name == '西双版纳州'):
        city_name = '西双版纳傣族自治州'
    if (city_name == '湘西州'):
        city_name = '湘西土家族苗族自治州'
    if (city_name == '伊犁哈萨克州'):
        city_name = '伊犁哈萨克自治州'
    if (city_name == '玉树州'):
        city_name = '玉树藏族自治州'
    if (city_name == '昌吉州'):
        city_name = '昌吉回族自治州'
    if (city_name == '阿坝州'):
        city_name = '阿坝藏族羌族自治州'
    city_geo = city_geocode.objects.values("city_geocode").get(city__contains=city_name)
    # print(city_geo)
    return JsonResponse({
        "city_geocode":city_geo,
    })

def History_data(request):
    city_name = request.GET.get("cityname")
    list = data_history.objects.filter(city_name=city_name).order_by('datetime').distinct()[:6]
    # print(list)
    data = []
    for item in list:
        item_dict = model_to_dict(item)
        data.append(item_dict)
    # print(data)
    return HttpResponse(json.dumps(data, ensure_ascii=False, cls=CJsonEncoder),content_type="application/json,charset-utf-8")

def Feedback(request):
    form = request.POST
    print(form)

    return JsonResponse({
        'status': 200
    })
#创建CJsonEcoder自定义类，处理datetime不可序列化问题
class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # 这里可以统一修改想要的格式
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            # 这里可以统一修改想要的格式
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)






