from django.conf.urls.defaults import patterns, url
#from agenda.apps.contactos import views

urlpatterns = patterns('agenda.apps.contactos.views',
   url(r'^$','index_view',name='vista_principal'),
    
)    
