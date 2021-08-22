from django.shortcuts import get_object_or_404, redirect, render
from membersites.models import Member, MemberServer, MemberServerForm, ApprovalStatus

# Create your views here.
def homepage(request):
    servers = MemberServer.objects.filter(status=ApprovalStatus.APPROVED)
    if request.method == 'POST':
        form = MemberServerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_server = form.save()
            return redirect('show_server', server_id=new_server.id, server_slug=new_server.slug)
    else:
        form = MemberServerForm()
    context = {
        'servers': servers,
        'form': form,
    }
    return render(request, 'index.html', context)

def list_servers(request):
    servers = MemberServer.objects.filter(status=ApprovalStatus.APPROVED)
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