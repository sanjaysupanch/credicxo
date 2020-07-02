from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, status, generics
from rest_framework.generics import * 
from .serializers import *
from .models import *

class BranchView(generics.ListCreateAPIView):
    queryset=branches.objects.all()[0:100]
    serializer_class=BranchDetailsSerializer

class BranchDetailsView(generics.ListAPIView):
    queryset=branches.objects.all()
    serializer_class=BranchDetailsSerializer
    # lookup_field="ifsc"

    def get_queryset(self, **kwargs):
        ifsc = self.kwargs['ifsc']
        return branches.objects.filter(ifsc=ifsc)

class BranchesListView(generics.ListCreateAPIView):
    queryset=bank_branches.objects.all()[0:100]
    serializer_class=BranchesSerializer
 
class BranchesView(generics.ListAPIView):
    queryset=bank_branches.objects.all()
    serializer_class=BranchesSerializer
    # lookup_field=('bank_name', 'city')

    def get_queryset(self, **kwargs):
        bank_name = self.kwargs['bank_name']
        city = self.kwargs['city']
        return bank_branches.objects.filter(bank_name=bank_name, city=city)

def redirect_view(request):
    response = redirect('/branches/')
    return response