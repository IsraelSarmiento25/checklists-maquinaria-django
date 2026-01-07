from rest_framework.routers import DefaultRouter
from .views import TractorViewSet, OperadorViewSet, ChecklistViewSet

router = DefaultRouter()
router.register('tractores', TractorViewSet)
router.register('operadores', OperadorViewSet)
router.register('checklists', ChecklistViewSet)

urlpatterns = router.urls
