from django.conf.urls import url, include
from django.contrib import admin

from nextcloudappstore.core.views import CategoryAppListView, \
    CategoryAppDetailView

urlpatterns = [
    url(r'^$', CategoryAppListView.as_view(), {'id': None}, name='home'),
    url(r'^', include('allauth.urls')),
    url(r'^categories/(?P<id>[\w]*)$', CategoryAppListView.as_view(),
        name='category-app-list'),
    url(r'^app/(?P<id>[\w_]+)$', CategoryAppDetailView.as_view(),
        name='category-app-detail'),
    url(r'^api/', include('nextcloudappstore.core.api.urls',
                          namespace='api')),
    url(r'^admin/', admin.site.urls),
]
