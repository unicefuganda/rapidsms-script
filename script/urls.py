from django.conf.urls.defaults import *
from  script.views import manage_script,edit_script

urlpatterns = patterns('',
    url(r"^manage_script/$",  manage_script, {'template':'script/script.html'},name="create_script"),
    url(r"^edit_script/(?P<script_pk>\w+)/$",  edit_script,name="edit_script"),
)
