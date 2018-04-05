from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('formlessness/', include('formlessness.urls')),
    path('admin/', admin.site.urls),
]
