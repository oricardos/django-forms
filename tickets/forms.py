from django import forms
from tempus_dominus.widgets import DatePicker

class TicketsForm(forms.Form):
    origin = forms.CharField(label="Origem", max_length=100)
    destiny = forms.CharField(label="Destino", max_length=100)
    departure_date = forms.DateField(label="Data de partida", widget=DatePicker())
    back_date = forms.DateField(label="Data de volta", widget=DatePicker())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'