from django.forms.models import modelformset_factory
from django.forms import ModelForm
from apps.hello.widgets import CalendarWidget
from hello.models import Person, Http_request


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'date': CalendarWidget(),
        }


class PriorityForm(ModelForm):
    class Meta:
        model = Http_request
        fields = ('priority',)

RequestEntryFormSet = modelformset_factory(
    Http_request,
    form=PriorityForm,
    fields=('priority',),
    extra=0
)
