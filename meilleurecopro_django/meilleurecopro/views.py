from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse

from meilleurecopro.condominium_expenses.services.estate_service import EstateService
from meilleurecopro.forms.stats_form import StatsForm
from meilleurecopro.forms.add_estate_form import AddEstateForm

def index(request):
    return HttpResponse("Hello, world. You're at the meilleure copro index.")


def stats_form(request):
    if request.method == 'POST':
        form = StatsForm(request.POST)

        if form.is_valid():
            location_type = form.cleaned_data['location_type']
            location = form.cleaned_data['location']

            return redirect(f"{reverse('stats_results')}?location={location}&location_type={location_type}")
    else:
        form = StatsForm()

    return render(request, 'meilleurecopro/stats_form.html', {'form': form})

def stats_results(request):
    location = request.GET.get('location')
    location_type = request.GET.get('location_type')
    condominium_expenses = EstateService().get_condominium_expenses(location, location_type)

    if condominium_expenses == None:
        raise Http404(f"Pas de résultats disponibles pour la localisation : {location} de type : {location_type}")
    
    return render(request, "meilleurecopro/stats_results.html", {"location": location, "stats": condominium_expenses})

def add_estate_form(request):
    if request.method == 'POST':
        form = AddEstateForm(request.POST)

        if form.is_valid():
            estate_service = EstateService()
            url = form.cleaned_data['estate_url']
            estate = estate_service.get_estate_by_url(url)
            estate_service.add_estate(estate)

            return HttpResponse("Bien immobilier ajouté à la base")
    else:
        form = AddEstateForm()
    
    return render(request, 'meilleurecopro/add_estate_form.html', {'form': form})
