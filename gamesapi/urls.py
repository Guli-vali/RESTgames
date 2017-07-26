from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('games.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
