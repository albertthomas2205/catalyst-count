from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .forms import UploadFileForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'account/users.html', {'users': users})
def home (request):
    users = User.objects.all()
    return render(request, 'account/users.html', {'users': users})





def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return redirect('upload_file')

            chunk_size = 1000  # Adjust the chunk size as needed
            file_data = pd.read_csv(csv_file, chunksize=chunk_size)
            
            for chunk in file_data:
                chunk = chunk.where(pd.notnull(chunk), None)  # Replace NaN with None

                companies = []
                for _, row in chunk.iterrows():
                    current_employee_estimate = row.get('current employee estimate')
                    total_employee_estimate = row.get('total employee estimate')

                    companies.append(Company(
                        name=row['name'],
                        domain=row['domain'],
                        industry=row['industry'],
                        size_range=row['size range'],
                        locality=row['locality'],
                        country=row['country'],
                        linkedin_url=row['linkedin url'],
                        current_employee_estimate=int(current_employee_estimate) if current_employee_estimate is not None else None,
                        total_employee_estimate=int(total_employee_estimate) if total_employee_estimate is not None else None
                    ))

                Company.objects.bulk_create(companies, batch_size=chunk_size)

            messages.success(request, 'File uploaded successfully')
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'account/fileupload.html', {'form': form})



from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company
from .serializers import CompanySerializer
from .filters import CompanyFilter
from rest_framework.response import Response

# class CompanyListView(generics.ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = CompanyFilter

#     def get(self, request, *args, **kwargs):
#         response = super().get(request, *args, **kwargs)
       
#         response_data = {
#             'count': self.filter_queryset(self.get_queryset()).count(),
#             'results': response.data
#         }
#         return Response(response_data)

# views.py
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['industry', 'size_range', 'locality', 'country']

from .forms import CompanyFilterForm

def index(request):
    print('haiiill')
    return render(request,'account/login.html')
