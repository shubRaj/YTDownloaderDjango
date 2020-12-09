from django.urls import path
from . import views
app_name="app_ytdownloader"
urlpatterns = [
    path("",views.YThome.as_view(),name="ytdownloader_home"),
]
