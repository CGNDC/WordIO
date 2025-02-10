from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def pinged(request):
    if request.method == "POST":
        data = json.loads(request.body)
        text = data.get("text", "")
        print(f"Received API request")
        print(f"cgndcDB received: {text}")
        return JsonResponse({"message": "cgndcDB Connection Healthy"})
    return JsonResponse({"error": "Invalid request"}, status=400)