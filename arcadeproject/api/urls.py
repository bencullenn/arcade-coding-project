from django.urls import path
from . import views

urlpatterns = [
    path("set", views.set, name="set"),
    path("get", views.get, name="get"),
    path("delete", views.delete, name="delete"),
    path("begin", views.begin, name="begin"),
    path("commit", views.commit, name="commit"),
    path("rollback", views.rollback, name="rollback"),
]
