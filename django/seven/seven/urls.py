from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^about/', 'profiles.views.about', name='about'),
    url(r'^contact/', 'profiles.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


