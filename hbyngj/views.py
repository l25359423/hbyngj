from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET
from product.controller import CategoryController, ProductController


@require_GET
def index_view(request, template_name='index.html'):

    categories = CategoryController.get_categories()

    products = ProductController.get_product_index(categories[0])

    return TemplateResponse(request,
                            template=template_name,
                            context={
                                "categories": categories,
                                "products": products,
                            })