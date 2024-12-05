
from dj_rest_auth.registration.views import ConfirmEmailView, VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import include, re_path, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('users.urls')),
    re_path(r'^api/categories/', include('category.urls')),
    re_path(r'^api/predict/', include('predict.urls')),
    re_path(r'^api/about/', include('about.urls')),
    re_path(r'^api/contactus/', include('contactus.urls')),
    re_path(r'^api/tag/', include('tag.urls')),
    re_path(r'^rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$',  ConfirmEmailView.as_view(), name='account_confirm_email'),
    re_path(r'^rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

