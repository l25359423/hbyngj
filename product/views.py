from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from product.controller import ProductController, CategoryController


def product(request, category_id='', template_name='product.html'):

    if not category_id:
        categories = CategoryController.get_categories()
        category = categories[0]
        category_id = category.id
    else:
        category = CategoryController.get_category(category_id)

    products = ProductController.get_product_by_category(category_id)
    return TemplateResponse(request,
                                template=template_name,
                                context={
                                    "products": products,
                                    "category": category,
                                })


def product_detail(request, product_id, template_name='product_detail.html'):
    try:
        product = ProductController.get_product(product_id)
    except ObjectDoesNotExist:
        raise Http404

    related_products = ProductController.get_product_by_category(product.category_id)
    related_products = related_products.filter(~Q(pk=product.id))

    return TemplateResponse(request,
                            template=template_name,
                            context={
                                "product": product,
                                "related_products": related_products,
                            })