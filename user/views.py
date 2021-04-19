import csv
import io
import json

from django.http import HttpResponse

from .models import User


# Create your views here.
def ViewAllUsers(request):
    alluser = User.objects.all()
    return HttpResponse(alluser)


def ViewUser(request, pk):
    try:
        selected_user = User.objects.get(id=pk)
    except:
        return HttpResponse(status=404, content="User not found")

    return HttpResponse(selected_user)


def AddUser(request):
    if request.method == 'POST':
        save_user = User()
        try:
            if json.loads(request.body)['name']:
                save_user.name = json.loads(request.body)['name']
        except:
            return HttpResponse(status=404, content="New user must have name")
        if json.loads(request.body)['age']:
            save_user.age = json.loads(request.body)['age']
            return HttpResponse(save_user)


def UpdateUser(request, pk):
    if request.method == 'PUT':
        try:
            selected_user = User.objects.get(id=pk)
        except:
            return HttpResponse(status=404, content="User Not Found")
        if selected_user:
            if json.loads(request.body)['age']:
                selected_user.age = json.loads(request.body)['age']

            if json.loads(request.body)['name']:
                selected_user.name = json.loads(request.body)['name']
            selected_user.save()

            return HttpResponse("create user successfully: {}".format(selected_user))


def DeleteUser(request, pk):
    if request.method == 'DELETE':
        try:
            selected_user = User.objects.get(id=pk)
        except:
            return HttpResponse(status=404, content="User Not Found")
        if selected_user:
            selected_user.delete()

            return HttpResponse("delete user successfully: {}".format(selected_user))


def ImportCsv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse(status=404, content="Must use csv file")
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        # import csv file without headers.
        try:
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                _, created = User.objects.update_or_create(
                    id=column[0],
                    name=column[1],
                    age=column[2]
                )
        except Exception:
            return HttpResponse(status=400, content="Import file failed")

        return HttpResponse(status=404, content="Import file successfully {}".format(csv_file))
