# lms/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    # Redirect the root URL to the course list
    path('', RedirectView.as_view(url='/courses/', permanent=True)),
]
