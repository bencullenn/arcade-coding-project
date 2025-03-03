from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from kv_store.store import Store
import json

store = Store(str, str)


# Create your views here.
@csrf_exempt
def set(request):
    # Verify the request method
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Parse the JSON request body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

    # Validate the request body
    if "key" not in data:
        return JsonResponse({"error": "Missing required parameter: key"}, status=400)

    if "value" not in data:
        return JsonResponse({"error": "Missing required parameter: value"}, status=400)

    # Set the key-value pair
    store.set(data["key"], data["value"])
    return JsonResponse({"message": "Key-value pair set successfully"})


def get(request):
    # Verify the request method
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Validate the request parameters
    key = request.query_params.get("key")
    if not key:
        return JsonResponse({"error": "Missing required parameter: key"}, status=400)

    value = store.get(key)
    return JsonResponse({"value": value})


@csrf_exempt
def delete(request):
    # Verify the request method
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Parse the JSON request body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

    # Validate the request parameters
    key = data.get("key")
    if not key:
        return JsonResponse({"error": "Missing required parameter: key"}, status=400)

    # Delete the key-value pair
    store.delete(key)
    return JsonResponse({"message": "Key-value pair deleted successfully"})


@csrf_exempt
def begin(request):
    # Verify the request method
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Start a new transaction
    store.begin()
    return JsonResponse({"message": "Transaction started"})


@csrf_exempt
def commit(request):
    # Verify the request method
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Commit the transaction
    store.commit()
    return JsonResponse({"message": "Transaction committed"})


@csrf_exempt
def rollback(request):
    # Verify the request method
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    # Rollback the transaction
    store.rollback()
    return JsonResponse({"message": "Transaction rolled back"})
