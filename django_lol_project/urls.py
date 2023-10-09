from champion_app.views import homeview, championpage
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls, name='admin_page' ),
    path('', homeview, name='homeview'),
    path('champion_page/', championpage, name='champion_page')

]