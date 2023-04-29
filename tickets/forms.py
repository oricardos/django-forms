from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from tickets.class_type import class_types
from tickets.validation import origin_destiny_equals, has_number, validate_date

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

    def clean(self):
        origin = self.cleaned_data.get('origin')
        destiny = self.cleaned_data.get('destiny')
        departure_date = self.cleaned_data.get('departure_date')
        back_date = self.cleaned_data.get('back_date')
        search_date = self.cleaned_data.get('search_date')

        errors_list = {}

        has_number(origin, 'origin', errors_list)
        has_number(destiny, 'destiny', errors_list)
        origin_destiny_equals(origin, destiny, errors_list)
        validate_date(departure_date, back_date, search_date, errors_list)

        if errors_list is not None:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.changed_data
