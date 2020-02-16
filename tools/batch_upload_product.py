# -*-coding: utf8 -*-
import os
import sys

import django
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hbyngj.settings")
django.setup()

from product.models import Product, Category

product_dir = "/Users/liuxiaoshuai/Downloads/yinengchn"

categories = os.listdir(product_dir)

for category_name in categories:

    category_name = category_name.decode("utf8")
    category = Category.objects.filter(name=category_name).first()

    if category:
        products = os.listdir(product_dir+"/"+category_name)
        for product_name in products:
            title = product_name.split(".")[0]
            product = Product()
            product.category = category
            product.visible = True
            product.title = title.encode('utf8')
            product.image.name = "product/"+product_name.encode("utf8")

            product.save()