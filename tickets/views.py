from django.shortcuts import render
from tickets.forms import TicketsForm

def index(request):
    form = TicketsForm()
    context = {'form': form}
    return render(request, 'index.html', context)
