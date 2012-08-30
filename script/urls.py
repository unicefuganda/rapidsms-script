from django.conf.urls.defaults import *
from .views import manage_script

urlpatterns = patterns('',
    url(r"^manage_script/$",  manage_script, {'template':'script/script.html'},name="create_script"),
)
