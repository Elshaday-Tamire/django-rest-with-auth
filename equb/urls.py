from django.urls import re_path
from . import views

urlpatterns = [
    re_path('addEqubType',views.addEqubType),
    re_path('addEqub',views.addEqub)
]
