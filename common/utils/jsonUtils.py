# JSON工具文件
import json

from django.http import JsonResponse


# 解决中文乱码
def get_json(json_):
    return JsonResponse(json_, json_dumps_params={'ensure_ascii': False})


# 序列化json
def load_json(request):
    return json.loads(request.body)
