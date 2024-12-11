"""
URL configuration for lawsyn project.

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
from django.contrib import admin
from django.urls import path, include
from main import views
from lawsyn import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rzadach', views.rzadach, name='rzadach'),
    path('reshebniki', views.reshebniki, name='reshebniki'),
    path('razrab', views.razrab, name='razrab'),
    path('ychebnik', views.ychebnik, name='ychebnik'),
    path('sbor', views.sbor, name='sbor'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('TextSave', views.TextSave, name='TextSave'),
    path('userHelp', views.userHelp, name='userHelp'),
    path('add_to_favorites/<int:book_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:book_id>/', views.remove_from_favorites, name='remove_from_favorites'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
