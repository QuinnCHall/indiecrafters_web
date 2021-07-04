from django.shortcuts import get_object_or_404, redirect, render
from membersites.models import MemberServer

# Create your views here.
def homepage(request):
    servers = MemberServer.objects.all()
    context = {
        'servers': servers,
    }
    return render(request, 'index.html', context)

def list_servers(request):
    servers = MemberServer.objects.all()
    context = {
        'servers': servers,
    }
    return render(request, 'server_list.html', context)

def show_server(request, server_id, server_slug):
    server = get_object_or_404(MemberServer, id=server_id)
    context = {
        'server': server,
    }
    return render(request, 'server.html', context)