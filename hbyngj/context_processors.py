from product.controller import CategoryController
from banner.controller import BannerController


def set_global_variable(request):
    categories = CategoryController.get_categories()
    banners = BannerController.get_banners()
    print(banners)
    return {
        "categories": categories,
        "banners": banners,
    }