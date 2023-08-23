from django.urls import path
from .views import NewsAll, NewsUpdate, NewsSlug

urlpatterns = [
    path('', NewsAll.as_view()),
    path('update/<int:pk>/', NewsUpdate.as_view(), ),
    path('<slug:slug>/', NewsSlug.as_view(), name='update'),
]
