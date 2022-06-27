from beeline_test2.views import UploadView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",UploadView.as_view()),
]
