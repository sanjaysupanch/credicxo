from django.urls import include, path
from .import views
from .views import *

urlpatterns=[
    
    path('', redirect_view, name='redirect_view'),
    path('branches/', BranchView.as_view(), name="branch-view"),
    path('branches/<ifsc>/', BranchDetailsView.as_view(), name="branch-update"),
    path('bank_branches/', BranchesListView.as_view(), name="branches-list"),
    path('bank_branches/<bank_name>/<city>/', BranchesView.as_view(), name="branches"),

]

