from champion_app.views import homeview, championpage
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls,name='admin' ),
    path('', homeview, name='homeview'),
    path('champion_page/', championpage, name='champion_page')

]
