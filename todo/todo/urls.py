from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework_swagger.views import get_swagger_view
from graphene_django.views import GraphQLView

schema_view = get_schema_view(title="Todo app",
                              description="API for all things",
                              version="1",
                              public=True,
                              permission_classes=[permissions.AllowAny])

schema_view_swagger = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/openapi/',
         schema_view,
         name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='userapp/swagger_ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='userapp/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),

    # path('redoc/',
    #      schema_view.with_ui('redoc', cache_timeout=0),
    #      name='schema-redoc'),


    path('api/userapp/', include('userapp.urls')),
    path('api/projectapp/', include('projectapp.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
