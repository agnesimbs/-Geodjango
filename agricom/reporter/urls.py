from django.urls import path
from   .views import *
urlpatterns=[
path('map/',MapPageView.as_view(),name='maps'),
path('county_data/',county_datasets,name='county'),
path('incidence_data/',point_datasets, name = 'incidences'),

]