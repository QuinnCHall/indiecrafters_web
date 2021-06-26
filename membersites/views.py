from django.shortcuts import get_object_or_404, redirect, render
from membersites.models import MemberSite

# Create your views here.
def homepage(request):
    return redirect('list_sites')

def list_sites(request):
    sites = MemberSite.objects.all()
    context = {
        'sites': sites,
    }
    return render(request, 'sites_list.html', context)

def show_site(request, site_id, site_slug):
    site = get_object_or_404(MemberSite, id=site_id)
    context = {
        'site': site,
    }
    return render(request, 'site.html', context)