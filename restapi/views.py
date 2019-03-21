from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from engine.main import Engine
from restapi.models import Member
# from restapi.api import MemberSerializer

# Create your views here.

engine = Engine()

@csrf_exempt
def test_REST(request):
    if request.method == 'GET':
        # restapi = Member.objects.all()
        chat = request.GET['chat']
        # serializer = MemberSerializer(restapi, many=True)\
        return HttpResponse(json.dumps(engine.chat_to_answer(chat),
                                        ensure_ascii=False), content_type="application/json; charset=utf-8")

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        # serializer = MemberSerializer(data=data)
        return JsonResponse('bye', status=400)
