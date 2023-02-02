from django.urls import path
from .views import AddPost, Retrieve

urlpatterns = [
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('retrieve/<int:pk>/', Retrieve.as_view(), name='retrieve')
]