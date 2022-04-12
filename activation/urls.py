"""
Copyright 2021 AKKA Technologies (philippe.szczech@akka.eu)

Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
the European Commission - subsequent versions of the EUPL (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence at:

https://joinup.ec.europa.eu/software/page/eupl

Unless required by applicable law or agreed to in writing, software
distributed under the Licence is distributed on an "AS IS" basis,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the Licence for the specific language governing permissions and
limitations under the Licence.
"""

from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()
router.register(r'flexibilityrequestactivation', views.FlexibilityRequestActivationViewSet)


urlpatterns = [
    path('flexibilityrequestactivationbyso/<str:so_name>/', views.FlexibilityRequestActivationBySoViewSet.as_view()),
    path('flexibilityactivationorder/', views.FlexibilityActivationOrderViewSet.as_view()),
    path('flexibilityactivationconfirmation/', views.FlexibilityActivationConfirmationViewSet.as_view()),
    path('registerflexibilityactivationrequest/', views.register_flexibility_activation_request),
    path('activatingrequest/', views.activation_testing),
]

urlpatterns += router.urls
