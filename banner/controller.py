from banner.models import Banner


class BannerController(object):
    @classmethod
    def get_banners(cls):
        return Banner.objects.filter(visible=True).order_by("-weight")

