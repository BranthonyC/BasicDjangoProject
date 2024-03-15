from django.urls import path
from .views import BookViewSet

urlpatterns = [
    path('libros', BookViewSet.as_view({'get': 'list'}), name='libros'),
    path('libros/<int:pk>', BookViewSet.as_view({'get': 'retrieve'}), name='libro_detralles'),
    path('libros/add', BookViewSet.as_view({'post': 'create'}), name='add'),
    path('libros/edit/<int:pk>', BookViewSet.as_view({'patch': 'partial_update'}), name='edit'),
    path('libros/delete/<int:pk>', BookViewSet.as_view({'delete': 'destroy'}), name='delete'),
    path('libros/soft/delete/<int:pk>', BookViewSet.as_view({'patch': 'partial_update'}), name='soft_delete'),
]