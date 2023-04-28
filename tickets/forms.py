from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from tickets.class_type import class_types

class TicketsForm(forms.Form):
    origin = forms.CharField(label="Origem", max_length=100)
    destiny = forms.CharField(label="Destino", max_length=100)
    departure_date = forms.DateField(label="Data de partida", widget=DatePicker())
    back_date = forms.DateField(label="Data de volta", widget=DatePicker())
    search_date = forms.DateField(label="Data da pesquisa", disabled=True, initial=datetime.today)
    class_type = forms.ChoiceField(label="TIpo de classe", choices=class_types)
    infos = forms.CharField(
        label="Informações extras",
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label="Email", max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

    def clean_origin(self):
        origin = self.cleaned_data.get('origin')
        if any(char.isdigit() for char in origin):
            raise forms.ValidationError('Origem inválida: Não inclua números')
        else:
            return origin