
from django.shortcuts import render, redirect, HttpResponse
from json import dumps
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
import folium
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import GaurdianForm, MemberForm, ModelForm
# Create your views here.


@login_required(login_url='/login')
def index(request):
    Member.objects.filter(retaled_to_id__isnull=True).delete()
    gdata = list(search.objects.values())
    mdata = list(Member.objects.values())
    mdataJSON = dumps(mdata)
    gdataJSON = dumps(gdata)
    userget = request.user.username
    return render(request, 'index.html', {'gdata': gdataJSON, 'mdata': mdataJSON, 'user': userget})


@login_required(login_url='/login')
def details(request, pk):
    userget = request.user.username
    search_id = search.objects.filter(id=pk)
    if search_id.count() > 0:
        a = search_id[0]
    else:
        a = 0
    member_id = Member.objects.filter(retaled_to_id=pk)
    # Map

    lat = a.lat
    lng = a.lng
    if lat == None or lng == None:
        return HttpResponse('Sorry,No Address Was added')
    else:
        # Create Map Object
        m = folium.Map(location=[11.1735, 75.8352], zoom_start=13)
        folium.Marker([lat, lng],).add_to(m)
        # Get HTML Representation of Map Object
        m = m._repr_html_()
        context = {
            'm': m,

        }
    return render(request, 'details.html', {'data': member_id, 'gdata': a, 'context': context, 'usi': userget})
    # data = Member.objects.filter(relate = pk)
    # return render(request, 'details.html', {'data': data})


@login_required(login_url='/login')
def location(request, pk):
    token = "sk.eyJ1IjoibW5hYmVlbDQ0NzciLCJhIjoiY2twZjc3dm16MGY2cjJwcmlqczgweXVuZyJ9.5jsQmGbQ4wDOHJ4hwUQa1Q"
    tileurl = 'https://api.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}@2x.png?access_token=' + str(
        token)
    search_id = search.objects.filter(id=pk)
    if search_id.count() > 0:
        a = search_id[0]
    else:
        a = 0
    lat = a.lat
    lng = a.lng
    if lat == None or lng == None:
        return HttpResponse('Sorry,No Address Was added')
    else:
        # Create Map Object
        m = folium.Map(location=[11.1735, 75.8352], zoom_start=13,
                       max_zoom=21, tiles=tileurl, attr='Mapbox')
        folium.Marker([lat, lng],).add_to(m)
        # Get HTML Representation of Map Object
        m = m._repr_html_()
        context = {
            'm': m,

        }
        return render(request, 'map.html', context)


@login_required(login_url='/login')
def CreateGaurdian(request):
    form = GaurdianForm()
    if request.method == 'POST':
        form = GaurdianForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/search/')
    context = {'form': form, 'stat': 'Add Gaurdian'}
    return render(request, 'create.html', context)


# Members Forms
@login_required(login_url='/login')
def CreateMember(request, pk):
    gad = search.objects.get(id=pk)
    form = MemberForm(request.POST or None, initial={
                      "house": gad.house, "retaled_to": gad.pk})
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('details', pk=pk)
    context = {'form': form, 'stat': 'Add Member'}
    return render(request, 'create.html', context)


@login_required(login_url='/login')
def updateGaurdian(request, pk):
    Search = search.objects.get(id=pk)
    form = GaurdianForm(instance=Search)
    if request.method == 'POST':
        form = GaurdianForm(request.POST, request.FILES, instance=Search)
        if form.is_valid():
            form.save()
            return redirect('details', pk=pk)
    context = {'form': form, 'pk': pk,
               'stat': 'Update or Delete', 'type': 'gad'}
    return render(request, 'update.html', context)


@login_required(login_url='/login')
def updateMember(request, pk, fk):
    Search = Member.objects.get(id=pk)
    form = MemberForm(instance=Search)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=Search)
        if form.is_valid():
            form.save()
            return redirect('details', pk=fk)
    context = {'form': form, 'pk': pk, 'fk': fk,
               'stat': 'Update or Delete', 'type': 'mem'}
    return render(request, 'update.html', context)


@login_required(login_url='/login')
def deleteGaurdian(request, pk):
    Search = search.objects.get(id=pk)

    if request.method == "POST":

        Search.delete()
        return redirect('/search/')
    context = {'item': Search, 'pk': pk, 'type': 'gad'}
    return render(request, 'delete.html', context)


@login_required(login_url='/login')
def deleteMember(request, pk):
    Search = Member.objects.get(id=pk)
    if request.method == "POST":
        Search.delete()
        return redirect('details', pk=Search.retaled_to_id)
    context = {'item': Search, 'pk': pk, 'type': 'mem'}
    return render(request, 'delete.html', context)


@login_required(login_url='/login')
def about(request):
    userget = request.user.username
    return render(request, 'about.html', {'user': userget})


def logout(request):
    auth.logout(request)
    return redirect('/')
