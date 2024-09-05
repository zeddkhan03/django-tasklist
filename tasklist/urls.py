from django.contrib import admin
from django.urls import path, include

# user-facing urls which go after ip & port
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
