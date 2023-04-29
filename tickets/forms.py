from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from tickets.class_type import class_types
from tickets.validation import origin_destiny_equals, has_number, validate_date
from tickets.models import Ticket, TravelClass, Person

class TicketsForm(forms.ModelForm):
    search_date = forms.DateField(label="Data da pesquisa", disabled=True, initial=datetime.today)

    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            'origin': 'Origem',
            'destiny': 'Destino',
            'departure_date': 'Data de partida',
            'back_date': 'Data de volta',
            'search_date': 'Data da pesquisa',
            'infos': 'Informações',
            'class_type': 'Tipo da Classe',
        }
        widgets = {
            'departure_date': DatePicker(),
            'back_date': DatePicker(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        origin = cleaned_data.get('origin')
        destiny = cleaned_data.get('destiny')
        departure_date = cleaned_data.get('departure_date')
        back_date = cleaned_data.get('back_date')
        search_date = cleaned_data.get('search_date')

        errors_dict = {}

        has_number(origin, 'origin', errors_dict)
        has_number(destiny, 'destiny', errors_dict)
        origin_destiny_equals(origin, destiny, errors_dict)
        validate_date(departure_date, back_date, search_date, errors_dict)

        for field, error_message in errors_dict.items():
            self.add_error(field, error_message)

        return cleaned_data