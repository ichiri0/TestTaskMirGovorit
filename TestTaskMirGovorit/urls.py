from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookbook/', include('cookbook.urls'), name="cookbook"),
]
