from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

def home(request):
    return HttpResponse("Добро пожаловать в API проекта Sessia!")

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Вы авторизованы!"})

schema_view = get_schema_view(
    openapi.Info(
        title="Sessia API",
        default_version='v1',
        description="Документация для API проекта Sessia",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@sessia.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # Подключение маршрутов приложения blog
    path('', home, name='home'),  # Корневой маршрут
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('protected/', ProtectedView.as_view(), name='protected'),  # Защищенный маршрут
]