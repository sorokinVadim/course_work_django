from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from urllib.parse import urlencode
from .forms import *
from rest_framework import viewsets
from .serializers import *


def offline(request):
    return render(request, 'base.html')


def home(request):
    clients = Client.objects.all()
    items = Item.objects.filter(owner=None)
    return render(request, 'pawnshop/home.html', {"clients": clients, "items": items})


def new_item(request):
    if request.method == "POST":
        post = request.POST
        form = ClientForm(post) if "client-form" in post else ItemForm(post)
        if form.is_valid():
            form.save()
            second_url = f"{reverse('new_item')}?{urlencode({'step': 2})}"
            return redirect(second_url if "client-form" in post else "home")
        step = request.GET.get("stem")
    else:
        step = request.GET.get("step", "")
        if step == '':
            args = urlencode({"step": 1})
            return redirect(f"{reverse('new_item')}?{args}")
        form = ClientForm() if request.GET.get("step") != "2" else ItemForm()
    return render(request, 'pawnshop/item_new.html', {"form": form, "step": step})


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ClientDetailView(DetailView):
    model = Client


class ItemDetailView(DetailView):
    model = Item
