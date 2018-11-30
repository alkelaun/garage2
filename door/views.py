from django.contrib import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views import View
from urllib.request import urlopen
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from revproxy.views import ProxyView

class DoorClass(View):

    template_name = 'door/door_trigger.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            response = str(urlopen('http://garage2:8080').read())[2:-3]
            messages.info(request, response)
        except:
            messages.error(request, 'Controller Offline')
        return render(request, self.template_name)

    def post(self, request):
        try:
            response = str(urlopen('http://garage2:8080/trigger').read())[2:-3]
            messages.success(request, response)
        except:
            messages.error(request, 'Door Failed to Trigger')
        return redirect('/door')

#The next two are attempts to proxy a ip camera.  The TextProxyView works, the first one is in progress.
class ViewClass(View):

    template_name = 'door/door_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TestProxyView(ProxyView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    upstream = 'http://192.168.0.14/'

