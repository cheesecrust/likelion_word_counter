from django.urls import path
import myapp.views

urlpatterns = [
    path('', myapp.views.index, name="index"),
    path('result/', myapp.views.result, name="result"),
]
