import io

from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http.response import FileResponse
from weasyprint import HTML
from markdown2 import markdown
from urllib.parse import urlencode
from .forms import *
from rest_framework import viewsets
from .serializers import *
from .data import get_text
from .tasks import update_items

from random import choice, randint
from datetime import datetime, timedelta

store = Storage(clients=Client.objects.all(), items=Item.objects.all())

def offline(request):
    return render(request, 'base.html')


def get_consignment(request, item_pk: int):
    item: Item = store.get_item(item_pk)
    if item is None:
        item = Item.objects.get(pk=item_pk)
    client = item.owner
    data = markdown(get_text(client, item))
    file = io.BytesIO()
    HTML(string=data).write_pdf(file)
    file.seek(0)
    return FileResponse(file, as_attachment=True, filename=f"{item.name}.pdf")


def home(request):
    clients: list[Client] = store.clients
    clients = Client.objects.all()
    items = Item.objects.filter(owner=None)
    return render(request, 'pawnshop/home.html', {"clients": clients, "items": items})


def new_item(request):
    if request.method == "POST":
        post = request.POST
        form = ClientForm(post) if "client-form" in post else ItemForm(post)
        if form.is_valid():
            item = form.save()
            store.add_item(item)
            second_url = f"{reverse('new_item')}?{urlencode({'step': 2})}"
            return redirect(second_url if "client-form" in post else "/")
        step = request.GET.get("stem")
    else:
        step = request.GET.get("step", "")
        if step == '':
            args = urlencode({"step": 1})
            return redirect(f"{reverse('new_item')}?{args}")
        form = ClientForm() if request.GET.get("step") != "2" else ItemForm()
    return render(request, 'pawnshop/item_new.html', {"form": form, "step": step})


def edit_item(request, pk):
    item: Item = store.get_item(pk)
    if item is None:
        item = Item.objects.get(pk=pk)
    if item is None:
        return redirect("home")
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ItemForm(instance=item)
    return render(request, 'pawnshop/item_edit.html', {"form": form, "save_until": item.save_until})


def edit_client(request, pk):
    item = Client.objects.get(pk=pk)
    if item is None:
        return redirect("home")
    if request.method == "POST":
        form = ClientForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ClientForm(instance=item)
    return render(request, 'pawnshop/item_edit.html', {"form": form})


def search(request):
    if request.method == "GET":
        form = SearchForm()
        return render(request, 'pawnshop/search.html', {"form": form, "data": []})
    form = SearchForm(request.POST)
    if form.data.get("item_name") != "":
        items = Item.objects.filter(name__iregex=form.data.get("item_name"))
        return render(request, 'pawnshop/search.html', {"form": form, "items": items})
    elif form.data.get("passport_num") != "":
        try:
            client = Client.objects.get(passport_num=form.data.get("passport_num"))
            return redirect('client', pk=client.pk)
        except:
            print("Passport num not fount")
    elif form.data.get("client_id") != "":
        try:
            return redirect('client', pk=form.data.get("client_id"))
        except:
            print("Client id not fount")
    elif form.data.get("item_id") != "":
        try:
            return redirect('item', pk=form.data.get("item_id"))
        except:
            print("Item id not fount")
    return render(request, 'pawnshop/search.html', {"form": form, "message": "Не знайдено!"})


def make_fake(request):
    count = request.GET.get("count")
    count = count if count is not None else 10
    client_names = ["Вася", "Петя", "Кристина", "Настя", "Диана", "Сережа", "Людмила"]
    item_names = ["Ноутбук", "Мышь", "Чашка", "PlayStation", "Стол", "Windows", "Колонки"]
    for i in range(count):
        client = Client(first_name=choice(client_names), last_name="", passport_num=randint(0, 99999999), age=randint(19, 100))
        client.save()
        for j in range(3):
            save_until = choice((datetime.now() - timedelta(days=3), datetime.now() + timedelta(days=3)))
            item = Item(name=choice(item_names), estimated_cost=randint(100, 100000), amount_pledged=randint(100, 10000),
                        save_until=save_until, owner=client)
            item.save()
        update_items()
    return redirect('home')


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
