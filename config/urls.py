from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
# from machina.app import board

from lib import views


urlpatterns = [
    # Package URLs
    url(r'^articles/comments/', include('django_comments.urls')),
    # url(r'^forums/', include('forums.urls', namespace='forums')),
    # url(r'^forum/', include(board.urls)),
    url(r'^forums/', include('simple_forums.urls', namespace='simple-forums')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),


    # CUSTOM URLS
    url(r'^lib-users/$', views.UserListView.as_view(), name='user-list'),
    url(r'^lib-users/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='user-detail'),

    url(r'^lib-books/$', views.BookListView.as_view(), name='book-list'),
    url(r'^lib-books/category/(?P<category_pk>\d+)/$', views.BookListView.as_view(), name='book-list'),
    url(r'^lib-books/author/(?P<author_pk>\d+)/$', views.BookListView.as_view(), name='book-list-author'),
    url(r'^lib-books/book/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^lib-books/book/(?P<pk>\d+)/book/(?P<user_pk>\d+)/$', views.BookBookView.as_view(), name='book-book'),
    url(r'^lib-books/book/(?P<pk>\d+)/unbook/$', views.BookUnbookview.as_view(), name='book-unbook'),
    url(r'^lib-books/book/(?P<pk>\d+)/rate/(?P<user_pk>\d+)/(?P<rating>\d+)$', views.BookRateView.as_view(), name='book-rate'),

    url(r'^lib-authors/$', views.AuthorListView.as_view(), name='author-list'),
    url(r'^lib-authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),

    url(r'^lib-threads/$', views.ThreadListView.as_view(), name='thread-list'),
    url(r'^lib-threads/(?P<pk>\d+)/$', views.ThreadDetailView.as_view(), name='thread-detail'),


    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('lib_social.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
