"""firstrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
# rest_framework_simplejwt module has to be installed separately using pip install djangorestframework_simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

model_viewset_router = DefaultRouter()
model_viewset_router.register('books_model_router', BookModelViewSet, basename='books_model_router')

viewset_router = DefaultRouter()
viewset_router.register('books_viewset_router', BookViewSet, basename='books_viewset_router')


urlpatterns = [
    path('books/',BookAPIView.as_view(), name='books'),
    path('books_details/<int:id>/', BookDetails.as_view(), name='books_details'), #here <int:id> id name is used the same must be used in BookDetails API Views
    path('generic_books/<int:pk>/', GenericAPIView.as_view(), name='generic_books'), #generic class variable name must be pk else set the `.lookup_field` attribute on the view correctly like lookup_field = 'id'
    path('book_viewset/', include(viewset_router.urls)),
    path('book_viewset/<int:pk>/', include(viewset_router.urls)),
    path('book_model_viewset/', include(model_viewset_router.urls)),
    #url with this /<int:pk>/ is not required for retrieve as model view set takes care of it
    path('get_token/', TokenObtainPairView.as_view(), name='get_token'), #called first with usename and password in body as post request
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'), 
    path('verify_token/', TokenVerifyView.as_view(), name='verify_token'),
    
]
