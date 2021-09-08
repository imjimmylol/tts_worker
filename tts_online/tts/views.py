from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .utils import chmodel
from .utils import enmodel
import logging
# Create your views here

# @csrf_exempt
# def hi(request):
#     print("ajax ok")
#
#     return HttpResponse("ok ok")


@csrf_exempt
def tts_api(request):
    msg = "hi"
    print("tts api")
    if request.method == "POST": #post 要大寫
        lang = request.POST.get('lang')
        txt=request.POST.get("text_input")
        if txt is None:
            return HttpResponse("no text input")

        if lang == "en":
            res = enmodel.en_ttw(txt)
            return JsonResponse(res)

        elif lang == "ch":
            res = chmodel.ch_ttw(txt)
            return JsonResponse(res)
    #logging.warning("no post :(")
    return HttpResponse(msg)

def demo(request):
    return render(request, "demo_front.html", locals())


