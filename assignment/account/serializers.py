from rest_framework import serializers
from .models import *
from rest_framework.serializers import HyperlinkedModelSerializer


class BankNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=banks
        fields=('name')


class BranchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=branches
        fields=('ifsc', 'branch', 'address', 'city', 'district', 'state')

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model=bank_branches
        fields=('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name')

