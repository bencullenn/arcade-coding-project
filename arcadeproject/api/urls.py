from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Key-value operations
    path("set/", views.set, name="set"),
    path("get/", views.get, name="get"),
    path("delete/", views.delete, name="delete"),
    # Transaction operations
    path("begin/", views.begin, name="begin"),
    path("commit/", views.commit, name="commit"),
    path("rollback/", views.rollback, name="rollback"),
]

# Add support for format suffixes (.json, .api, etc.)
urlpatterns = format_suffix_patterns(urlpatterns)
