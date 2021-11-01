from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .tasks import add
# Create your views here.

class MyView(View):
    def get(self, request):
        print("start do request")
        # CourseTask().apply_async(args=("hello",), queue="work_queue")
        add.delay(1, 2)
        print("end do request")
        return JsonResponse({"result": "ok"})