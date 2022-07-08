from django.urls import path
from .views import *
from categories.views import *

app_name="store"

urlpatterns = [
    path('index/', index, name = "index"),
    path('checkout/', checkout,name = "checkout"),
    path('details/<int:id>',product_details,name = "details"),   
    path("search/", SearchResultsView.as_view(), name="search"),
    path("category/<int:id>/",CategoryView.as_view(),name="category"),
    path("search/search-filter", searchFilter ,name="search-filter"),
    path("search/one", one ,name="one"),
    path("search/two", two ,name="two"),
    path("search/three", three ,name="three"),
    path("search/four", four ,name="four"),
    path("search/five", five ,name="five"), 
]
