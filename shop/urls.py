from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>/item/', views.ItemView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/', views.ItemRUDView.as_view()),
    path('category/<int:category_id>/item/<int:pk>/order/', views.OrderListCreateView.as_view()),
    path('category/<int:category_id>/item/<int:item_pk>/order/<int:pk>/', views.OrderRUDView.as_view()),
]
