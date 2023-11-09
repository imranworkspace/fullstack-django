from rest_framework import routers
from django.urls import path,include

from .views import StudentView

router = routers.DefaultRouter()
router.register('students',StudentView,basename='students')

urlpatterns = [
    path('',include(router.urls))    
]