
from django.contrib import admin
from django.urls import path
from django.conf.urls import include  # added


urlpatterns = [
    path('', include('memories_api.urls')),  # added
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))  # added
]
