from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_v2 import (
    DepartmentManagerViewSet, TicketTypeViewSet, TicketViewSet,
    CommentViewSet, AttachmentViewSet, FAQCategoryViewSet, FAQViewSet
)

router = DefaultRouter()
router.register(r'departmentmanagers', DepartmentManagerViewSet)
router.register(r'tickettypes', TicketTypeViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'faqcategories', FAQCategoryViewSet)
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
