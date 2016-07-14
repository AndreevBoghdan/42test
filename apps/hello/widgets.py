from django.forms import DateInput


class CalendarWidget(DateInput):
    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui-1.10.4.custom.min.js',
            'js/calendar.js',
        )
        css = {
            'all': ('css/jquery-ui-1.10.4.custom.css', )
        }
