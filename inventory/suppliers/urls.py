from django.urls import path
from . import views

app_name = "suppliers"

urlpatterns = [
    path("add/", views.add_supplier, name="add_supplier"),
    path("all/", views.suppliers_page, name="suppliers_page"),
    path("<supplier_id>/", views.supplier_page, name="supplier_page"),
]