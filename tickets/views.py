from django.shortcuts import render
from tickets.forms import TicketsForm, PersonForm

def index(request):
    """
    Renderiza a página inicial do sistema de tickets, onde o usuário pode criar um novo ticket.
    
    Args:
        request (HttpRequest): objeto de requisição do Django.
    
    Returns:
        HttpResponse: uma resposta HTTP que renderiza o template 'index.html', com um formulário de criação de tickets sendo passado no context.
    """
    form = TicketsForm()
    person_form = PersonForm
    context = {'form': form, 'person_form': person_form}
    return render(request, 'index.html', context)

def data(request):
    """
    View que recebe uma requisição POST com dados do formulário TicketsForm. Se o formulário for válido,
    renderiza a página data.html com o contexto contendo o formulário preenchido. Caso contrário,
    renderiza a mesma página com os erros do formulário exibidos.
    
    Args:
    - request: objeto HttpRequest contendo os detalhes da requisição HTTP recebida.
    
    Returns:
    - Um objeto HttpResponse contendo o conteúdo HTML renderizado.
    """
    if request.method == 'POST':
        form = TicketsForm(request.POST)
        person_form = PersonForm(request.POST)
        if form.is_valid():
            context = {'form': form, 'person_form': person_form}
            print(context)
            return render(request, 'data.html', context)
        else:
            context = {'form': form, 'person_form': person_form}
            return render(request, 'index.html', context)
