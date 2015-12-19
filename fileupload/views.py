# encoding: utf-8
import json

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from .models import File, SingleUseToken
from .response import JSONResponse, response_mimetype
from .serialize import serialize


class FileCreateView(CreateView):
    model = File
    fields = "__all__"

    def dispatch(self, *args, **kwargs):
        print(kwargs['token_id'])
        self.token = get_object_or_404(SingleUseToken, token=kwargs['token_id'])
        return super(FileCreateView, self).dispatch(*args, **kwargs)

    # Adds the token to the context
    def get_context_data(self, *args, **kwargs):
        context_data = super(FileCreateView, self).get_context_data(
            *args, **kwargs)
        context_data.update({'token': self.token})
        return context_data

    def form_valid(self, form):
        print("Valid")
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

class AngularVersionCreateView(FileCreateView):
    template_name_suffix = '_angular_form'

class FileDeleteView(DeleteView):
    model = File

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class FileListView(ListView):
    model = File

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
