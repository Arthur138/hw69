import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.

# def json_echo_view(request, *args, **kwargs):
#     if request.method == 'GET':
#         data = json.loads(request.body)
#         data_json = list(data.values())
#
#         data_as_json = json.dumps(data_json)
#         response = HttpResponse(data_as_json)
#         response['Content-Type'] = 'application/json'
#         return response

def add(request, *args, **kwargs):
    if request.body:
        try:
            data = json.loads(request.body)
            data_json = list(data.values())
            result = {
                "answer": int(data_json[0]) + int(data_json[1])
            }
        except ValueError:
            result = {
                'Error': 'Enter two numbers please'
            }
        response = JsonResponse({'result':result})
        return response

def subtract(request, *args, **kwargs):
    if request.body:
        try:
            data = json.loads(request.body)
            data_json = list(data.values())
            result = {
                'answer' : int(data_json[0]) - int(data_json[1])
            }
        except ValueError:
            result = {
                'Error': 'Enter two numbers please'
            }
        response = JsonResponse({'result':result})
        return response

def multiply(request, *args, **kwargs):
    if request.body:
        try:
            data = json.loads(request.body)
            data_json = list(data.values())
            result = {
                "answer": int(data_json[0]) * int(data_json[1])
            }
        except ValueError:
            result = {
                'Error': 'Enter two numbers please'
            }
        response = JsonResponse({'result':result})
        return response


def divide(request, *args, **kwargs):
    if request.body:
        try:
            data = json.loads(request.body)
            data_json = list(data.values())
            result = {
                "answer": int(data_json[0]) / int(data_json[1])
            }
        except ZeroDivisionError:
            result = {
                'Error': 'Division by zero!'
            }
        except ValueError:
            result = {
                'Error': 'Enter two numbers please'
            }
        response = JsonResponse({'result':result})
        return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')