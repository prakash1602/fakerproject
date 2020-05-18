from django.shortcuts import render, redirect
from .models import Employee
import faker

fake = faker.Faker()


# Create your views here.
def inserting_data(request):

    for i in range(10):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        salary = fake.random_element(elements=(20000, 15000, 30000, 40000, 50000))
        job = fake.random_element(elements=('HR', 'TL', 'MANAGER', 'SE', 'SSE', 'PM'))
        location = fake.random_element(elements=('hyd', 'mum', 'che', 'Pune', 'bang'))

        data = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            salary=salary,
            job=job,
            location=location
        )
        data.save()
    return redirect('/')


def fetching__data(request):
    employees = Employee.objects.all()
    return render(request, 'employee_data.html', {'employees': employees})
