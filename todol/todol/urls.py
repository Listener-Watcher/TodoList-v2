from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from todolist import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^accounts/profile/$', 'newsletter.views.profile', name='profile'),
    url(r'^about/$', 'todolist.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^todolist/$', 'todolist.views.dashboard', name='todolist'),
    url(r'^todolist/details/(?P<id>\w{0,50})/$', 'todolist.views.details'),
    url(r'^todolist/add/$', 'todolist.views.add', name='add'),
    url(r'^dashboard/$', 'todolist.views.dashboard', name='dashboard'),
    url(r'^todolist/deletion/(?P<id>\w{0,50})/$', 'todolist.operations.delete'),
    url(r'^todolist/done/(?P<id>\w{0,50})/$', 'todolist.operations.done'),
    url(r'^todolist/edition/(?P<id>\w{0,50})/$', 'todolist.operations.edit', name='edit'),
    # url(r'^todolist/$', views.TaskList.as_view()),
    url(r'^todolist/api/$', views.TaskList.as_view()),
    url(r'^todolist/api/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    # url(r'^todolist/$', include('todolist.urls')),
]
urlpatterns += format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
