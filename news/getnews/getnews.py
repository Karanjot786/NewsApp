# from .news_sites.getpolitico import getpolitico
# from .news_sites.getfox import getfox
# from .news_sites.getnatreview import getnatreview
# from .news_sites.getslate import getslate
# from .news_sites.getcnndailywire import getcnndailywire
# from .news_sites.getnypost import getnypost
# from .news_sites.getnpr import getnpr
# from .news_sites.getmsnbc import getmsnbc
# from .news_sites. import getoan
from .news_sites.getcbs import getcbs, indin, world, sports, business
# from .news_sites.business import business
# # from .news_sites.indin import indin, world
# from .news_sites.sports import sports
# from .news_sites.getreason import getreason
from ..models import Headline


def get_news():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    getcbs(per_site)


def get_business():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    business(per_site)

def get_indin():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    indin(per_site)

def get_sports():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    sports(per_site)

def get_world():
    STORIES = 25
    SITES = 1
    per_site = STORIES // SITES

    Headline.objects.all().delete()
    world(per_site)