from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import estadoViewSet, cidadeViewSet, pessoaViewSet

router = DefaultRouter()
router.register(r"estados", estadoViewSet)
router.register(r"cidades", cidadeViewSet)
router.register(r"pessoas", pessoaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),

]
