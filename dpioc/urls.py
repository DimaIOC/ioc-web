import static as static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('rosetta/', include('rosetta.urls')),
    path('summernote/', include('django_summernote.urls')),
    ]

urlpatterns += i18n_patterns(
    path('', include('landing.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



