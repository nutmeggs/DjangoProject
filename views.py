from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Asset
from .forms import AssetForm
from django.contrib import messages

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact Us',
            'message': 'Contact Page.',
            'year': datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )

def calculate_due_date(hire_date):
    return hire_date + timedelta(days=30)

def studenthome(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.Due_Date = calculate_due_date(asset.Hire_Date)
            asset.requested = True 
            asset.save()
            messages.info(request, 'Item Added')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('studenthome')
    else:
        form = AssetForm()
    context = {
        'title': 'home',
        'message': 'The student home page.',
        'year': datetime.now().year,
        'form': form
    }
    return render(request, 'app/studenthome.html', context)

def dashboard(request):
    assets = Asset.objects.filter(requested=False)
    requested_assets = Asset.objects.filter(requested=True)
    overdue_assets = Asset.objects.filter(Due_Date__lt=timezone.now())
    return render(
        request,
        'app/dashboard.html',
        {
            'title': 'Dashboard',
            'message': 'Dashboard page.',
            'year': datetime.now().year,
            'assets': assets,
            'requested_assets': requested_assets,
            'overdue_assets': overdue_assets,
        }
    )

def delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    asset.delete()
    return redirect('dashboard')

def approve_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    asset.requested = False
    asset.save()
    return redirect('dashboard')
