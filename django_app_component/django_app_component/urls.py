from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TODO/', include("TODO.urls")),
    path('COM/', include("COM.urls")),
]
