from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from django.urls import path,include

from api import views
router = routers.DefaultRouter()
router.register('students',views.StudentView,basename='students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('',include('api.urls')),
]
