from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['industry', 'size_range', 'locality', 'country']
   
    
from django.shortcuts import render


from django.core.cache import cache

def company_list_view(request):
    distinct_industries = cache.get('distinct_industries')
    if not distinct_industries:
        distinct_industries = list(Company.objects.values('industry').distinct()[:10])
        cache.set('distinct_industries', distinct_industries, 60 * 60)  # Cache for 1 hour

    distinct_localities = cache.get('distinct_localities')
    if not distinct_localities:
        distinct_localities = list(Company.objects.values('locality').distinct()[:10])
        cache.set('distinct_localities', distinct_localities, 60 * 60)

    distinct_size_ranges = cache.get('distinct_size_ranges')
    if not distinct_size_ranges:
        distinct_size_ranges = list(Company.objects.values('size_range').distinct()[:10])
        cache.set('distinct_size_ranges', distinct_size_ranges, 60 * 60)

    distinct_countries = cache.get('distinct_countries')
    if not distinct_countries:
        distinct_countries = list(Company.objects.values('country').distinct()[:10])
        cache.set('distinct_countries', distinct_countries, 60 * 60)

    context = {
        "industries": distinct_industries,
        "localities": distinct_localities,
        "size_ranges": distinct_size_ranges,
        "countries": distinct_countries
    }
    
    return render(request, 'account/company_list.html', context)



from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from app.models import Company
from app.serializers import CompanySerializer
from django_filters import rest_framework as filters

class CompanyFilter(filters.FilterSet):
    class Meta:
        model = Company
        fields = ['industry', 'size_range', 'locality', 'country']

class CompanyCountView(APIView):
    filter_backends = [DjangoFilterBackend]

    def get(self, request, *args, **kwargs):
        filter_backends = [DjangoFilterBackend()]
        filterset = CompanyFilter(request.GET, queryset=Company.objects.all())
        print("haiiiiiii")

        if filterset.is_valid():
            queryset = filterset.qs
        else:
            queryset = Company.objects.none()  # Return an empty queryset if filters are invalid

        count = queryset.count()
       
        
        return Response({'count': count})