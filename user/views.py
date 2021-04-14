from .models import User
from django.http import HttpResponse
import json


# Create your views here.
def ViewAllUsers(request):
    alluser = User.objects.all()
    return HttpResponse(alluser)


def ViewUser(request, id):
    try:
        selected_user = User.objects.get(id=id)
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


def UpdateUser(request, id):
    if request.method == 'PUT':
        try:
            selected_user = User.objects.get(id=id)
        except:
            return HttpResponse(status=404, content="User Not Found")
        if selected_user:
            if json.loads(request.body)['age']:
                selected_user.age = json.loads(request.body)['age']

            if json.loads(request.body)['name']:
                selected_user.name = json.loads(request.body)['name']
            selected_user.save()

            return HttpResponse("create user successfully: {}".format(selected_user))


def DeleteUser(request, id):
    if request.method == 'DELETE':
        try:
            selected_user = User.objects.get(id=id)
        except:
            return HttpResponse(status=404, content="User Not Found")
        if selected_user:
            selected_user.delete()

            return HttpResponse("delete user successfully: {}".format(selected_user))
