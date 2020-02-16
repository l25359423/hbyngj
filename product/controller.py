from product.models import Category, Product


class CategoryController(object):
    @classmethod
    def get_category(cls, category_id):
        return Category.objects.get(pk=category_id)

    @classmethod
    def get_categories(cls):
        return Category.objects.filter(visible=True).order_by("-weight")


class ProductController(object):
    @classmethod
    def get_product(cls, product_id):
        return Product.objects.get(pk=product_id)

    @classmethod
    def get_product_index(cls, category):
        return Product.objects.filter(category=category, visible=True)[0:12]

    @classmethod
    def get_product_by_category(cls, category):
        return Product.objects.filter(category_id=category, visible=True)
