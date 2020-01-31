import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core.validators import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from rest_framework import viewsets
from django.views.generic import TemplateView, CreateView, DetailView
from main.models import Store, Task
from main.forms import (StoreSignUpForm,
                        UserForm,
                        UserEditForm,
                        StoreForm,
                        TaskForm,
                        DeliveryBoyForm)


# from store.tasks import store_created_new_task_notification
# Create your views here.


def celery_task_checker(request):
    return render(request, 'celery.html')


def home(request):
    try:
        if request.user.store:
            return redirect(store_home)
    except Exception as e:

        # elif request.user.delivery_boy:
        return redirect(delivery_boy_home)


def get_auth_token(request):
    return redirect(store_home)


@login_required(login_url='/store/signin')
def store_home(request):
    return redirect(store_tasks)


def store_signup(request):
    if request.method == "POST":
        store_user_form = StoreSignUpForm(request.POST)
        if store_user_form.is_valid:
            store = store_user_form.save()
            store.refresh_from_db()
            store.save()
            raw_password = store_user_form.cleaned_data.get('password1')
            store = authenticate(username=store.username, password=raw_password)
            login(request, store)
            return redirect(store_home)
    else:
        store_user_form = StoreSignUpForm()

    return render(request, "store/store_signup.html",
                  {"store_user_form": store_user_form})


@login_required(login_url='/store/signin/')
def store_account(request):
    user_form = UserEditForm(instance=request.user)
    store_form = StoreForm(instance=request.user.store)

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        store_form = StoreForm(request.POST, instance=request.user.store)
        if user_form.is_valid() and store_form.is_valid():
            user_form.save()
            store_form.save()
    return render(request, 'store/store_account.html',
                  {'user_form': user_form, 'store_form': store_form})


@login_required(login_url='/store/signin/')
def create_task(request):
    task_form = TaskForm()
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            # task_instance = Task.objects.create(**task_form.cleaned_data)
            task_instance = task_form.save(commit=False)
            task_instance.store = request.user.store
            task_instance.status = Task.ACCEPTED
            task_instance.save()
            messages.success(request, 'New Task Created')
            # store_created_new_task_notification.delay(task_instance.id)
            return redirect(store_home)

    return render(request, 'store/create_task.html', {'task_form': task_form})


@login_required(login_url="/store/signin")
def store_tasks(request):
    print("user")
    print(request.user.store)
    if request.method == "POST":
        pass
    # tasks = Task.objects.filter(store=request.user.store).order_by("-id")
    tasks = Task.objects.filter(store=request.user.store).order_by("-id")
    return render(request, "store/tasks.html", {"tasks": tasks})


@login_required(login_url="/store/signin")
def store_task(request, id):
    task = Task.objects.get(id=id, store=request.user.store)
    return render(request, "store/task.html", {"task": task})


def delivery_boy_signup(request):
    user_form = UserForm()
    delivery_boy_form = DeliveryBoyForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        delivery_boy_form = DeliveryBoyForm(request.POST)

        if user_form.is_valid() and delivery_boy_form.is_valid():
            new_user_instance = User.objects.create_user(**user_form.cleaned_data)
            delivery_boy_instance = delivery_boy_form.save(commit=False)
            delivery_boy_instance.user = new_user_instance
            delivery_boy_instance.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))
            return redirect(delivery_boy_home)
    return render(request, "deliver/delivery_boy_signup.html",
                  {"user_form": user_form, "delivery_boy_form": delivery_boy_form})


@login_required(login_url='/deliver/signin')
def delivery_boy_home(request):
    return redirect(deliver_tasks)
    # return render(request, "deliver/tasks.html")


@login_required(login_url='/deliver/signin')
def delivery_boy_account(request):
    user_form = UserEditForm(instance=request.user)
    delivery_boy_form = DeliveryBoyForm(
        instance=request.user.delivery_boy)

    if request.method == "POST":
        user_form = UserEditForm(
            request.POST, instance=request.user)
        delivery_boy_form = DeliveryBoyForm(
            request.POST, instance=request.user.delivery_boy)
        if user_form.is_valid() and delivery_boy_form.is_valid():
            user_form.save()
            delivery_boy_form.save()
    return render(request, 'deliver/delivery_boy_account.html',
                  {'user_form': user_form, 'delivery_boy_form': delivery_boy_form})


@login_required(login_url="/deliver/signin")
def deliver_tasks(request):
    tasks = Task.objects.filter(delivery_boy=None).exclude(
        Q(status=Task.RETURN) | Q(status=Task.DELIVERED)).order_by('-created_at')
    accepted_tasks = Task.objects.filter(
        status=Task.PICKUP, delivery_boy=request.user.delivery_boy).order_by('-created_at')
    completed_tasks = Task.objects.filter(
        status=Task.DELIVERED, delivery_boy=request.user.delivery_boy).order_by('-created_at')
    return render(request, "deliver/tasks.html",
                  {"tasks": tasks,
                   "accepted_tasks": accepted_tasks,
                   "completed_tasks": completed_tasks})


class TaskDetails(DetailView):
    template_name = 'store/task_details.html'
    model = Task
    context_object_name = 'task'


def roothome(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def whygobd(request):
    return render(request, 'whygobd.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')

# def handler404(request, *args, **argv):
#     response = render_to_response('custom_404_view.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response
#
# def handler500(request, *args, **argv):
#     response = render_to_response('custom_404_view.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response
