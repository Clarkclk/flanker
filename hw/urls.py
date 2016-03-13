from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hw.views.home', name='home'),
    # url(r'^hw/', include('hw.foo.urls')),
    url(r'^$', 'hw.hw.index'),
    url(r'^hw/$', 'hw.hw.indexhw'),
    url(r'^taskpage/$','hw.list.index'),
    url(r'^taskpage/addpage$','hw.addpage.index'),
    url(r'^taskpage/modifypage/[\w]+$','hw.modifypage.index'),
    url(r'^taskpage/infopage/[\w]+$','hw.infopage.index'),
    url(r'^prepage/$','hw.addedge.index'),
    url(r'^loginpage/$', 'hw.check.check'),
    url(r'^storepage/$', 'hw.store.store'),
    url(r'^workpage/$', 'hw.work.work'),
    url(r'^configpage/$', 'hw.config.config'),
    url(r'^loadpage/$', 'hw.load.load'),
    url(r'^showpage/$', 'hw.show.show'),
    url(r'^registerpage/$', 'hw.register.register'),
    url(r'^dag/$', 'hw.dag.index')
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
