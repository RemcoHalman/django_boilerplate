from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
from decouple import config, Csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('website.urls')),
]

admin.site.site_header = "Website Managment".upper()
admin.site.site_title = "Portfolio"
admin.site.index_title = "Management"

handler400 = 'website.views.error_400_view'
handler403 = 'website.views.error_403_view'
handler404 = 'website.views.error_404_view'
handler500 = 'website.views.error_500_view'


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
