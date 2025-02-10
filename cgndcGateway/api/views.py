from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def ping_db(request):
    url = "http://127.0.0.1:8002/api/"
    data = json.loads(request.body)
    text = data.get("text", "")
    response = requests.post(url, json={"text": text})
    if response.status_code == 200:
        return JsonResponse({"message": "Success DB"})
    return JsonResponse({"error": "Failed to send"}, status=500)

@csrf_exempt
def ping_ml(request):
    url = "http://127.0.0.1:8003/api/"
    data = json.loads(request.body)
    text = data.get("text", "")
    response = requests.post(url, json={"text": text})
    if response.status_code == 200:
        return JsonResponse({"message": "Success"})
    return JsonResponse({"error": "Failed to send"}, status=500)