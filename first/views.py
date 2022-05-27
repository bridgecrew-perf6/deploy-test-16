from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
import pygsheets
from .models import *
from django.shortcuts import redirect


def index_page(request):
    st = status.objects.all()
    context = {"st": st}
    return render(request, "index.html", context)


def reboot_status_page(request):
    gc = pygsheets.authorize(service_file='secret.json')
    sh = gc.open_by_key('1HhRBqMXxmE2uA06pNKc1HI1lnBAgJkfGKABGqmAhJAQ')
    wks = sh.worksheet_by_title('Status')
    length = len(wks.get_all_values())
    todo = wks.get_values('AC6', 'AC{}'.format(length))
    done = wks.get_values('AB6', 'AB{}'.format(length))
    contrag = wks.get_values('X6', 'X{}'.format(length))
    time = wks.get_values('AA6', 'AA{}'.format(length))
    amount_cars = wks.get_values('Y6', 'Y{}'.format(length))
    num_cars = wks.get_values('Z6', 'Z{}'.format(length))
    for item in status.objects.all():
        item.delete()
    for i in range(len(done)):
        item = status(id=i + 1, ToDo=float(todo[i][0]), Done=float(done[i][0]), Contrag=contrag[i][0],
                      Time=time[i][0], Amount_Cars=amount_cars[i][0], Num_Cars=num_cars[i][0])
        item.save()
    return redirect('/')


def weights_page(request):
    weightsModel_all = weights.objects.all()
    context = {"weightsModel_all": weightsModel_all}
    return render(request, "weights.html", context)


def reboot_weights_page(request):
    gc = pygsheets.authorize(service_file='secret.json')
    sh = gc.open_by_key('1HhRBqMXxmE2uA06pNKc1HI1lnBAgJkfGKABGqmAhJAQ')
    wks = sh.worksheet_by_title('Weights')
    length = len(wks.get_all_values())
    time = wks.get_values('K5', 'K{}'.format(length))
    material = wks.get_values('B5', 'B{}'.format(length))
    mass = wks.get_values('J5', 'J{}'.format(length))
    car_num = wks.get_values('H5', 'H{}'.format(length))
    contrag = wks.get_values('D5', 'D{}'.format(length))
    pba = wks.get_values('F5', 'F{}'.format(length))

    for item in weights.objects.all():
        # print(item)

        item.delete()
    for i in range(len(material)):
        item = weights(id=i + 1, Time=time[i][0], Material=material[i][0], Mass=float(mass[i][0]),
                       Contrag=contrag[i][0], Car_Num=car_num[i][0], PBA=pba[i][0])
        item.save()
    return redirect('weights/')



def income_page(request):
    incomeModel_all = income.objects.all()
    context = {"incomeModel_all": incomeModel_all}
    return render(request, "income.html", context)


def reboot_income_page(request):
    gc = pygsheets.authorize(service_file='secret.json')
    sh = gc.open_by_key('1HhRBqMXxmE2uA06pNKc1HI1lnBAgJkfGKABGqmAhJAQ')
    wks = sh.worksheet_by_title('Weights')
    length = len(wks.get_all_values())
    time = wks.get_values('AD6', 'AD{}'.format(length))
    material = wks.get_values('AB6', 'AB{}'.format(length))
    mass = wks.get_values('AE6', 'AE{}'.format(length))
    contrag = wks.get_values('AC6', 'AC{}'.format(length))
    stock = wks.get_values('AA6', 'AA{}'.format(length))

    for item in income.objects.all():
        item.delete()
    for i in range(len(material)):
        item = income(id=i + 1, Time=time[i][0], Material=material[i][0], Mass=float(mass[i][0]),
                       Contrag=contrag[i][0], Stock=stock[i][0])
        item.save()
    return redirect('income/')


def task(request):
    driverModel_all = driver.objects.all()
    context = {"driverModel_all": driverModel_all}
    if request.method == 'POST':
        selected_car_nums = request.POST.getlist('selected_car_nums')
        print(selected_car_nums)
    return render(request, 'task.html', context)


    # return render(request, 'task.html')
    # print(driverModel_all)
    # driverModel_all = weights.objects.all()
    # print(driverModel_all)
    # ms = ['mango', 'apple', 'watermelon']
