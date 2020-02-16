from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET


@require_GET
def index_view(request, template_name='index.html'):
    agent = request.META.get('HTTP_USER_AGENT', None)

    return TemplateResponse(request,
                            template=template_name,
                            context={

                            })