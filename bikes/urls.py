from django.urls import path,include
from bikes import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('bike',views.BikeViewSet)

urlpatterns=[
    path('',include(router.urls))
]

