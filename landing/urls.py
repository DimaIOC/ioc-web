from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboute, name='about'),
    path('eservices/', views.eservices, name='eservices'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.single_news, name='single_news'),
    path('team/', views.team, name='team'),
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
