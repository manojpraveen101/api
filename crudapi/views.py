
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from crudapi.models import Employee
from crudapi.serializers import EmployeeSerializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        firstname = request.GET.get('firstname',None)
        if firstname is not None:
            employee = employee.filter(firstname=firstname)
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse({"message": "valid"})
        else:
            return JsonResponse({ "message":"not valid"})

    elif request.method == 'DELETE':
        firstname = request.GET.get('firstname', None)
        employee = Employee.objects.filter(firstname=firstname)
        if firstname is not None:
            employee.delete()
            return JsonResponse({"message":"deleted successfully"})
        else:
            return JsonResponse({"message":"deletion not successful"})

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        firstname = employee_data.get("firstname")
        if firstname is not None:
            employee = Employee.objects.filter(firstname=firstname)
            employee.update(**employee_data)
            return JsonResponse({"message":"updated successful"})
        else:
            return JsonResponse({"message":"update failed"})
