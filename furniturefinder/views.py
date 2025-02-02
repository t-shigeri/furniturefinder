from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RoomPhoto, Furniture
from .forms import FurnitureSearchForm  # ここでインポート

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def gallery(request):
    photos = RoomPhoto.objects.filter(user=request.user)
    return render(request, 'gallery.html', {'photos': photos})

def services(request):
    return render(request, 'services.html')

def reference(request):
    return render(request, 'reference.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    form = FurnitureSearchForm(request.GET)
    results = []
    if form.is_valid():
        min_height = form.cleaned_data.get('min_height')
        max_height = form.cleaned_data.get('max_height')
        min_width = form.cleaned_data.get('min_width')
        max_width = form.cleaned_data.get('max_width')
        style = form.cleaned_data.get('style')

        results = Furniture.objects.all()
        if min_height:
            results = results.filter(height__gte=min_height)
        if max_height:
            results = results.filter(height__lte=max_height)
        if min_width:
            results = results.filter(width__gte=min_width)
        if max_width:
            results = results.filter(width__lte=max_width)
        if style:
            results = results.filter(style__icontains=style)

    return render(request, 'search.html', {'form': form, 'results': results})

