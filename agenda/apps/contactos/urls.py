from django.conf.urls.defaults import patterns, url
#from agenda.apps.contactos import views

urlpatterns = patterns('agenda.apps.contactos.views',
   url(r'^$','home', name='home'),
   url(r'^agregar/$', 'add', name='add'),
   url(r'^editar/(?P<contact_id>\d+)/$', 'add', name='update'),
   url(r'^borrar/(?P<contact_id>\d+)/$', 'delete', name='delete'),
)    
