import re
from models import Http_request


def directory(path):
    result = re.findall(r'/\w+/', path)
    try:
        return result[0]
    except IndexError:
        return ""


def not_static(path):
    return (directory(path) != '/static/') and (directory(path) != '/uploads/')


class Request_save(object):

    def process_request(self, request):
        path = request.path
        if (not request.is_ajax()) and not_static(path):
            Http_request.objects.create(path=request.path, meth=request.method)

    def process_response(self, request, response):
        if (not request.is_ajax()) and not_static(request.path):
            path = Http_request.objects.latest("date")
            path.status_code = response.status_code
            path.save()
        return response
