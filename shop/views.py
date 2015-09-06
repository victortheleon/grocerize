from django.shortcuts import render
from shop.models import Buyer, Seller
from django.http import HttpResponse
# Create your views here.
API_KEY = "AIzaSyBSnxR51eqb3VtGGFe6bBclOR3OUsLiLC0"
REQUEST_URL = "https://maps.googleapis.com/maps/api/distancematrix/json?"
REQUEST_PARAMETERS = {
    "key": API_KEY
}
import urllib, urllib2


def index(request):
    uname = request.GET.get("uname")
    buyer = Buyer.objects.get(login_email=uname)
    address = buyer.active_address
    sellers = Seller.objects.all()
    REQUEST_PARAMETERS["origins"] = address.address_line1+"+"+address.address_line2+"+"+address.city+\
        "+"+address.state+"+"+address.country+"+"+str(address.zip)
    REQUEST_PARAMETERS["destinations"] = "|".join([seller.active_address.address_line1+"+"
                                                   +seller.active_address.address_line2 +
                                                   "+"+seller.active_address.city+\
        "+"+seller.active_address.state+"+"+seller.active_address.country+"+"
                                                   +str(seller.active_address.zip) for seller in sellers])
    url = REQUEST_URL+urllib.urlencode(REQUEST_PARAMETERS)
    print url
    res = urllib2.urlopen(url).read()
    return HttpResponse(res, content_type='application/JSON')