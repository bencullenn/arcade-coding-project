from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import KeyValueSerializer, KeySerializer, TransactionSerializer
from kv_store.store import Store

store = Store(str, str)


@api_view(["POST"])
def set(request):
    """
    Set a key-value pair in the store.
    """
    serializer = KeyValueSerializer(data=request.data)
    if serializer.is_valid():
        store.set(serializer.validated_data["key"], serializer.validated_data["value"])
        return Response({"message": "Key-value pair set successfully"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get(request):
    """
    Get a value by key from the store.
    """
    key = request.query_params.get("key")
    if not key:
        return Response(
            {"error": "Missing required parameter: key"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    value = store.get(key)
    return Response({"value": value})


@api_view(["POST"])
def delete(request):
    """
    Delete a key-value pair from the store.
    """
    serializer = KeySerializer(data=request.data)
    if serializer.is_valid():
        store.delete(serializer.validated_data["key"])
        return Response({"message": "Key-value pair deleted successfully"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def begin(request):
    """
    Begin a new transaction.
    """
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        store.begin()
        return Response({"message": "Transaction started"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def commit(request):
    """
    Commit the current transaction.
    """
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        store.commit()
        return Response({"message": "Transaction committed"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def rollback(request):
    """
    Rollback the current transaction.
    """
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        store.rollback()
        return Response({"message": "Transaction rolled back"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
