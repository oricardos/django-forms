from django import forms

class TicketsForm(forms.Form):
    origin = forms.CharField(label="Origem", max_length=100)
    destiny = forms.CharField(label="Destino", max_length=100)
    departure_date = forms.DateField(label="Data de partida")
    back_date = forms.DateField(label="Data de volta")