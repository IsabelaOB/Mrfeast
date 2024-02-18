
from django.contrib import admin
from django.urls import path
from food import views as foodViews
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', foodViews.login_view, name='login'),
    path('nombre_de_la_url/', foodViews.home_view, name='nombre_de_la_url'),
    path('nombre_de_la/', TemplateView.as_view(template_name='page.html'), name='nombre_de_la'),
    # Puedes agregar más URLs según tus necesidades
]
