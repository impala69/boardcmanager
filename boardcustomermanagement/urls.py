"""boardcustomermanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cmanager import views
from django.views.static import serve
from boardcustomermanagement import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addgame', views.addgame),
    url(r'^refine', views.refine_users),
    url(r'^info', views.info),
    url(r'^deleterow', views.delete_row),
    url(r'^userinfo', views.user_info),
    url(r'^gencode', views.generate_gift_code),
    url(r'^lottery-list', views.lottery_list),
    url(r'^lottery', views.lottery),
    url(r'^user_gifts', views.user_gifts),
    url(r'^give_prize', views.give_prize),
    url('', views.home),
    url(r'public/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
