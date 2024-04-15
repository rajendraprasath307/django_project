from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.
import json
from user_details.models import Registermodel, Contact_details, Address_details, Vendor_details


# value get and update method--------------------------------------------------------------
@csrf_exempt
@api_view(['POST', 'GET'])
def Register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if "id" not in data:
            obj = Registermodel.objects.create(firstname=data['firstname'],
                                               lastname=data['lastname'],
                                               userid=data['userid'],
                                               password=data['password'],
                                               mblenum=data['mblenum'],
                                               email=data['email'])
            response_data = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(response_data))
        else:
            obj = Registermodel.objects.filter(id=data['id']).update(firstname=data['firstname'],
                                                                     lastname=data['lastname'],
                                                                     userid=data['userid'],
                                                                     password=data['password'],
                                                                     mblenum=data['mblenum'],
                                                                     email=data['email'])
            response_data = [{'Message': 'Data updated'}]
            return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def AddressDetails(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if "id" not in data:
            obj = Address_details.objects.create(line1=data['line1'],
                                                 line2=data['line2'],
                                                 pincode=data['pincode'],
                                                 state=data['state'],
                                                 district=data['district'],
                                                 city=data['city'],
                                                 created_by=data['created_by'])

            response_data = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(response_data))
        else:
            obj = Address_details.objects.filter(id=data['id']).update(line1=data['line1'],
                                                                       line2=data['line2'],
                                                                       pincode=data['pincode'],
                                                                       state=data['state'],
                                                                       district=data['district'],
                                                                       city=data['city'],
                                                                       created_by=data['created_by'])

            response_data = [{'Message': 'Data updated'}]
            return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def ContactDetails(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if "id" not in data:
            obj = Contact_details.objects.create(mobileno=data['mobileno'],
                                                 emailid=data['emailid'],
                                                 accountno=data['accountno'],
                                                 beneficaryname=data['beneficaryname'],
                                                 created_by=data['created_by'])

            response_data = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(response_data))
        else:
            obj = Contact_details.objects.filter(id=data['id']).update(mobileno=data['mobileno'],
                                                                       emailid=data['emailid'],
                                                                       accountno=data['accountno'],
                                                                       beneficaryname=data['beneficaryname'],
                                                                       created_by=data['created_by'])

            response_data = [{'Message': 'Data update'}]
            return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def VendorDetails(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if "id" not in data:
            obj = Vendor_details.objects.create(vendorname=data['vendorname'],
                                                vendorcode=data['vendorcode'],
                                                vendorgst=data['vendorgst'],
                                                vendorpan=data['vendorpan'],
                                                vendorbranch=data['vendorbranch'],
                                                vendoraddress_id=data['vendoraddress'],
                                                vendorcontact_id=data['vendorcontact'],
                                                created_by=data['created_by'])

            response_data = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(response_data))
        else:
            obj = Vendor_details.objects.filter(id=data['id']).update(vendorname=data['vendorname'],
                                                                      vendorcode=data['vendorcode'],
                                                                      vendorgst=data['vendorgst'],
                                                                      vendorpan=data['vendorpan'],
                                                                      vendorbranch=data['vendorbranch'],
                                                                      vendoraddress_id=data['vendoraddress'],
                                                                      vendorcontact_id=data['vendorcontact'],
                                                                      created_by=data['created_by'])

            response_data = [{'Message': 'Data updated'}]
            return HttpResponse(json.dumps(response_data))


# value get method filter(all values)---------------------------------
@csrf_exempt
@api_view(['GET'])
def Get_Register(request):
    if request.method == "GET":
        obj = Registermodel.objects.filter()
        response_data = []
        for i in obj:
            data = {
                "firstname": i.firstname,
                "lastname": i.lastname
            }
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['GET'])
def Get_AddressDetails(request):
    if request.method == "GET":
        obj = Address_details.objects.all()
        response_data = []
        for i in obj:
            data = {
                "pincode": i.pincode,
                "state": i.state,
                "city": i.city
            }
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['GET'])
def Get_ContactDetails(request):
    if request.method == "GET":
        obj = Contact_details.objects.all()
        response_data = []
        for i in obj:
            data = {
                "mobileno": i.mobileno,
                "emailid": i.emailid,
                "accountno": i.accountno
            }
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['GET'])
def Get_VendorDetails(request):
    if request.method == "GET":
        obj = Vendor_details.objects.all()
        response_data = []
        for i in obj:
            data = {
                "vendorname": i.vendorname,
                "vendoraddress": {
                    "field1": i.vendoraddress.line1,
                    "field2": i.vendoraddress.line2
                },
                "vendorcontact": {
                    "contact": i.vendorcontact.emailid
                },
                "vendorcode": i.vendorcode,
                "vendorgst": i.vendorgst,
                "vendorpan": i.vendorpan
            }
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))


# particular get value method (particular id details) ---------------------------------------------------
@csrf_exempt
@api_view(['GET'])
def NewMethod(request, pk):
    if request.method == "GET":
        response_data = []
        obj = Registermodel.objects.get(id=pk)
        data = {
            "firstname": obj.firstname,
            "lastname": obj.lastname
        }
        response_data.append(data)
    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['GET'])
def NewAddressMethod(request, pk):
    if request.method == "GET":
        obj = Address_details.objects.get(id=pk)
        response_data = []
        data = {
            "pincode": obj.pincode,
            "state": obj.state,
            "city": obj.city
        }
        response_data.append(data)
    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['GET'])
def NewContactMethod(request, pk):
    if request.method == "GET":
        obj = Contact_details.objects.get(id=pk)
        response_data = []
        data = {
            "emailid": obj.emailid,
            "accountno": obj.accountno,
            "mobileno": obj.mobileno
        }
        response_data.append(data)
    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['GET'])
def NewVendorMethod(request, pk):
    if request.method == "GET":
        obj = Vendor_details.objects.get(id=pk)
        response_data = []
        data = {
            "vendorgst": obj.vendorgst,
            "vendorpan": obj.vendorpan,
            "vendorbranch": obj.vendorbranch
        }
        response_data.append(data)
    return HttpResponse(json.dumps(response_data))


# html page creation and manipulation----------------------
@csrf_exempt
@api_view(['POST', 'GET'])
def Index_function(request):
    if request.method == "GET":
        a1 = request.GET.get('firstname')
        obj = Registermodel.objects.filter(firstname__icontains=a1)
        response_data = []
        for i in obj:
            data = {
                "firstname": i.firstname,
                "lastname": i.lastname
            }
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))
    return render(request, 'index.html')


# particular search value method---------------------------
@csrf_exempt
@api_view(['POST', 'GET'])
def SearchRegister(request):
    if request.method == "GET":
        a1 = request.GET.get('firstname')
        obj = Registermodel.objects.filter(firstname__icontains=a1)
        response_data = []
        for i in obj:
            data = {
                "firstname": i.firstname,
                "lastname": i.lastname
            }
            response_data.append(data)
    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def SearchAddress(request):
    if request.method == "GET":
        a1 = request.GET.get('line1')
        obj = Address_details.objects.filter(line1__icontains=a1)
        response_data = []
        for i in obj:
            data = {
                "line1": i.line1,
                "line2": i.line2,
                "state": i.state,
                "district": i.district
            }
            response_data.append(data)
    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def SearchContact(request):
    if request.method == "GET":
        a1 = request.GET.get('beneficaryname')
        obj = Contact_details.objects.filter(beneficaryname__icontains=a1)
        response_data = []
        for i in obj:
            data = {
                "beneficaryname": i.beneficaryname,
                "emailid": i.emailid
            }
            response_data.append(data)

    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def SearchVendor(request):
    if request.method == "GET":
        a1 = request.GET.get('vendorname')
        obj = Vendor_details.objects.filter(vendorname__icontains=a1)
        response_data = []
        for i in obj:
            data = {
                "vendorname": i.vendorname,
                "vendorcode": i.vendorcode,
                "vendorpan": i.vendorpan,
                "vendorbranch": i.vendorbranch
            }
            response_data.append(data)
    return HttpResponse(json.dumps(response_data))


# particular delete value method---------------------------

@csrf_exempt
@api_view(['DELETE'])
def DeleteRegister(request, pk):
    if request.method == "DELETE":
        deleted = Registermodel.objects.filter(id=pk).delete()
        if deleted:
            response_data = [{'Message': 'Data Deleted'}]

        else:
            response_data = [{'Message': 'No Data Found to Deleted'}]
            return HttpResponse(json.dumps(response_data))
        return HttpResponse(json.dumps(deleted))


@csrf_exempt
@api_view(['DELETE'])
def DeleteAddress(request, pk):
    if request.method == "DELETE":
        deleted = Address_details.objects.filter(id=pk).delete()

        if deleted:
            response_data = [{'Message': 'Data Deleted'}]
        else:
            response_data = [{'Message': 'No Data Found to Deleted'}]
            return HttpResponse(json.dumps(response_data))
        return HttpResponse(json.dumps(deleted))


@csrf_exempt
@api_view(['DELETE'])
def DeleteContact(request, pk):
    if request.method == "DELETE":
        deleted = Contact_details.objects.filter(id=pk).delete()
        if deleted:
            response_data = [{'Message': 'Data Deleted'}]
        else:
            response_data = [{'Message': 'No Data Found to Deleted'}]
        return HttpResponse(json.dumps(deleted))


@csrf_exempt
@api_view(['DELETE'])
def DeleteVendor(request, pk):
    if request.method == "DELETE":
        deleted = Vendor_details.objects.filter(id=pk).delete()
        if deleted:
            response_data = [{'Message': 'Data Deleted'}]
        else:
            response_data = [{'Message': 'No Data Found to Deleted'}]

        return HttpResponse(json.dumps(response_data))


# particular search value (multiple condition) method---------------------------

@csrf_exempt
@api_view(['POST', 'GET'])
def Multi_search_register(request):
    if request.method == "GET":
        value1 = request.GET.get('firstname')
        value2 = request.GET.get('userid')
        value3 = request.GET.get('email')
        query = Q()
        if value1:
            query |= Q(firstname__icontains=value1)

        if value2:
            query |= Q(userid__icontains=value2)

        if value3:
            query |= Q(email__icontains=value3)

        obj = Registermodel.objects.filter(query)

        response_data = []
        for i in obj:
            data = {
                "firstname": i.firstname,
                "userid": i.userid,
                "email": i.email
            }
            response_data.append(data)

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def Multi_search_address(request):
    if request.method == "GET":
        value1 = request.GET.get('state')
        value2 = request.GET.get('district')
        value3 = request.GET.get('city')
        query = Q()
        if value1:
            query |= Q(state__icontains=value1)
        if value2:
            query |= Q(district__icontains=value2)
        if value3:
            query |= Q(city__icontains=value3)

        obj = Address_details.objects.filter(query)

        response_data = []

        for i in obj:
            data = {
                "state": i.state,
                "district": i.district,
                "city": i.city
            }
            response_data.append(data)

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def Multi_search_contact(request):
    if request.method == "GET":
        value1 = request.GET.get('mobileno')
        value2 = request.GET.get('emailid')
        value3 = request.GET.get('accountno')
        query = Q()
        if value1:
            query |= Q(mobileno__icontains=value1)
        if value2:
            query |= Q(emailid__icontains=value2)
        if value3:
            query |= Q(accountno__icontains=value3)

        obj = Contact_details.objects.filter(query)

        response_data = []

        for i in obj:
            data = {
                "mobileno": i.mobileno,
                "emailid": i.emailid,
                "accountno": i.accountno
            }
            response_data.append(data)

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def Multi_search_vendor(request):
    if request.method == "GET":
        value1 = request.GET.get('vendorname')
        value2 = request.GET.get('vendorgst')
        value3 = request.GET.get('vendorpan')
        query = Q()
        if value1:
            query |= Q(vendorname__icontains=value1)
        if value2:
            query |= Q(vendorgst__icontains=value2)
        if value3:
            query |= Q(vendorpan__icontains=value3)

        obj = Vendor_details.objects.filter(query)

        response_data = []

        for i in obj:
            data = {
                "vendorname": i.vendorname,
                "vendorgst": i.vendorgst,
                "vendorpan": i.vendorpan
            }
            response_data.append(data)

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST'])
def Login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        obj = Registermodel.objects.filter(userid=data["userid"], password=data["password"])
        if not obj.exists():
            response_data = [{'Message': 'Data not Created'}]

        else:
            response_data = [{'Message': 'Data Created'}]
        return HttpResponse(json.dumps(response_data))
