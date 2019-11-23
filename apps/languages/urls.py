from django.urls import path, include
from rest_framework import routers
from .views import LanguageView, ParadigmView, ProgrammerView

router = routers.DefaultRouter()
router.register('language', LanguageView)
router.register('paradigm', ParadigmView)
router.register('programmer', ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]