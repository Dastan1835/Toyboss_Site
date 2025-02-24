"""
URL configuration for toybos_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.i18n import set_language

from toybos_products.views import ProductView, ProductDetailView, HomeView, AboutView, PublicationsView, PublicationsInnerView, RecipesView, RecipesInnerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('set-language/', set_language, name='set_language'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('publications/', PublicationsView.as_view(), name='publications'),
    path('publications/<int:pk>/', PublicationsInnerView.as_view(), name='publications-detail'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipesInnerView.as_view(), name='recipes-detail'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
