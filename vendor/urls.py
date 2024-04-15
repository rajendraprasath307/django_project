"""
URL configuration for vendor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')).
"""
from django.contrib import admin
from django.urls import path
from user_details import views as tnapp

urlpatterns = [
    path('admin/', admin.site.urls),

    # value get and update------------------------------------
    path('Register', tnapp.Register, name='Register'),
    path('Address_details', tnapp.AddressDetails, name='Address_details'),
    path('Contact_details', tnapp.ContactDetails, name='Contact_details'),
    path('Vendor_details', tnapp.VendorDetails, name='Vendor_details'),
    # value get method--------------------------------------
    path('Get_register', tnapp.Get_Register, name='Get_register'),
    path('Get_address_details', tnapp.Get_AddressDetails, name='Get_address_details'),
    path('Get_contact_details', tnapp.Get_ContactDetails, name='Get_contact_details'),
    path('Get_vendor_details', tnapp.Get_VendorDetails, name='Get_vendor_details'),
    # particular get value method---------------------------

    path('New_Method/<pk>', tnapp.NewMethod, name='New_Method'),
    path('New_Address_details/<pk>', tnapp.NewAddressMethod, name='New_Address_Details'),
    path('New_Contact_details/<pk>', tnapp.NewContactMethod, name='New_Contact_Details'),
    path('New_Vendor_details/<pk>', tnapp.NewVendorMethod, name='New_Vendor_Details'),
    # html page creation and manipulation----------------------

    path('index', tnapp.Index_function, name='INDEX'),
    # particular search value method---------------------------

    path('Search_Register', tnapp.SearchRegister, name='search_register'),
    path('Search_Address', tnapp.SearchAddress, name='search_address'),
    path('Search_Contact', tnapp.SearchContact, name='search_contact'),
    path('Search_Vendor', tnapp.SearchVendor, name='search_vendor'),
    # particular search value method(multiple condition)---------------------------

    path('Multi_Search_Register', tnapp.Multi_search_register, name='multi_search_register'),
    path('Multi_Search_address', tnapp.Multi_search_address, name='multi_search_address'),
    path('Multi_Search_contact', tnapp.Multi_search_contact, name='multi_search_contact'),
    path('Multi_Search_vendor', tnapp.Multi_search_vendor, name='multi_search_vendor'),
    # particular delete value method---------------------------

    path('Delete_Register/<pk>', tnapp.DeleteRegister, name='delete_register'),
    path('Delete_Address/<pk>', tnapp.DeleteAddress, name='delete_address'),
    path('Delete_Contact/<pk>', tnapp.DeleteContact, name='delete_contact'),
    path('Delete_Vendor/<pk>', tnapp.DeleteVendor, name='delete_vendor'),

    path('LOGIN', tnapp.Login, name='login')
]
