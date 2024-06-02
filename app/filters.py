import django_filters
from .models import Company

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            'industry': ['exact'],
            'size_range': ['exact'],
            'locality': ['exact'],
            'country': ['exact'],
        }
