import requests
from django.http import JsonResponse

def ping_db(request):
    url = "http://127.0.0.1:8001/api/db/"
    text_to_send = "Pinged from frontend!"
    response = requests.post(url, json={"text": text_to_send})
    if response.status_code == 200:
        return JsonResponse({"message": "Success"})
    return JsonResponse({"error": "Failed to send"}, status=500)

def ping_ml(request):
    url = "http://127.0.0.1:8001/api/ml/"
    text_to_send = "Pinged from frontend!"
    response = requests.post(url, json={"text": text_to_send})
    if response.status_code == 200:
        return JsonResponse({"message": "Success"})
    return JsonResponse({"error": "Failed to send"}, status=500)