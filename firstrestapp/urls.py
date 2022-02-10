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
from django.urls import path
from .views import *

urlpatterns = [
    path('books/',BookAPIView.as_view(), name='books'),
    path('books_details/<int:id>/', BookDetails.as_view(), name='books_details'), #here <int:id> id name is used the same must be used in BookDetails API Views
    path('generic_books/<int:pk>/', GenericAPIView.as_view(), name='generic_books'), #generic class variable name must be pk else set the `.lookup_field` attribute on the view correctly like lookup_field = 'id'
]
