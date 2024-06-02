from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet
from .views import company_list_view,CompanyCountView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = [
 
    path('companies/', company_list_view, name='company_list_view'),
    path('api/companies/count/', CompanyCountView.as_view(), name='company-count'),
    # Ensure your app's URLs are included here
]