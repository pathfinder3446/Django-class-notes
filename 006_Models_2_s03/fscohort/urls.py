from django.urls import path, include
from .views import fscohort, subfolder


urlpatterns = [
        path('', fscohort),
        path('subfolder/', subfolder),
   
]
