import json
from django.shortcuts import render_to_response, redirect, render
from django.http.response import HttpResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest
from hello.forms import PersonForm
from hello.models import Person, Http_request
from hello.forms import RequestEntryFormSet
import hello.signals  # noqa

# Create your views here.


def main(request):
    return render(request,
                  'hello/person.html',
                  {'person': Person.objects.first()}
                  )


def requests(request):
    args = {}
    http_requests = Http_request.objects.all()[:10]
    args["http_requests"] = http_requests
    request.META["CSRF_COOKIE_USED"] = True
    if request.is_ajax():
        data = json.dumps({'sucess': False})
        if request.method == 'POST':
            for elem in http_requests:
                path = Http_request.objects.get(pk=elem.pk)
                if not path.is_read:
                    path.is_read = True
                    path.save(update_fields=['is_read'])
            return HttpResponse("OK")
        elif request.method == 'GET':
            if not isinstance(data, type(None)):
                data = serialize('json', http_requests)
            return HttpResponse(data)
    return render_to_response('hello/requests.html', args)


@login_required
def edit_person(request):
    if Person.objects.first() is None:
        contact = Person()
    else:
        contact = Person.objects.first()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse("OK")
            else:
                return redirect(reverse('hello.views.main'))
        else:
            return HttpResponseBadRequest(json.dumps(form.errors))
    else:
        form = PersonForm(instance=contact)
    return render(request, 'hello/edit.html', {'form': form})


@login_required
def request_priority(request, page_number=1):
    args = {}
    if request.method == 'POST':
        formset = RequestEntryFormSet(request.POST)

        if formset.is_valid():
            formset.save()

        return redirect(reverse('hello.views.requests'))
    else:
        requests = Http_request.objects.all()
        paginator = Paginator(requests, 10)
        current_page = paginator.page(page_number)
        ten_requests = current_page.object_list
        formset = RequestEntryFormSet(queryset=ten_requests)
        objects = zip(ten_requests, formset)
        args = {'objects': objects, 'formset': formset,
                "pages": paginator.page(page_number)}
        return render(request, "hello/priority.html", args)
