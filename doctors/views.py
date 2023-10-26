from django.http import HttpResponse
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.template import loader
from .forms import FestivalForm
from .models import Footballer, Statistics, Clubs


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def search(request):
    name = request.GET.get("name", "")
    data = Footballer.objects.all().filter(name__contains=name).values()
    template = loader.get_template('pages/search.html')
    context = {
        'data': data,
        'name': name,
    }

    return HttpResponse(template.render(context=context))


def all(request):
    context = {
        "dataset": Footballer.objects.all()
    }

    return render(request, "pages/all.html", context)


def detail_view(request, id):
    context = {
        "data": Footballer.objects.get(id=id)
    }

    return render(request, "pages/detail_view.html", context)


def details(request, id):
    player = Footballer.objects.get(id=id)
    ans = Statistics.objects.filter(f_name=player.name).values()
    template = loader.get_template('pages/details.html')
    context = {
        'ans': ans,
        'player': player,
    }

    return HttpResponse(template.render(context, request))


def create_view(request):
    context = {}
    form = FestivalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/all')
    context['form'] = form
    return render(request, "pages/create_view.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Footballer, id=id)
    form = FestivalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/'+str(id))
    context["form"] = form

    return render(request, "pages/update_view.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Footballer, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "pages/delete_view.html", context)
