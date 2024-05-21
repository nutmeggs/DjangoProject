"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.forms import AddAssetForm
from app.models import Asset
from django.contrib import messages

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact Us',
            'message':'Contact Page.',
            'year':datetime.now().year,
        }
    )

def dashboard(request):
    """Renders the about dash."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dashboard.html',
        {
            'title':'Dashboard',
            'message':'dashboard page.',
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

#def studenthome(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/studenthome.html',
#        {
#            'title':'home',
#            'message':'The student home page.',
#            'year':datetime.now().year,
#        }
#    )

def studenthome(request):
    if request.method == 'POST':
        form = AddAssetForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            messages.info(request, 'Item Added')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('studenthome')
    else:
        form = AddAssetForm()
        context = {'form':form}
        return render(request,'app/studenthome.html', context)
