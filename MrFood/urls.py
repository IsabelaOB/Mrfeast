from django.contrib import admin
from django.urls import path
from food import views as foodViews
from django.views.generic import TemplateView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
    path('login/', foodViews.login_view, name='login'),
    path('form/', foodViews.home_view, name='form'),
    path('portal/', foodViews.portal_view, name='portal'),
    path('contacto/', foodViews.contacto_view, name='contacto')
]


urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)