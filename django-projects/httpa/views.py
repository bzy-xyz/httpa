from django.http import HttpResponse
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import sys
import sha
from xmlrpclib import *

def hello(request):
    pxy = ServerProxy("http://httpa.csail.mit.edu:3631")
    res = {0:"Success", 1:"Capacity", 2:"Again"}
    key = Binary(sha.new("colors").digest())
    val = Binary("red")
    secret = ""
    ttl = 9999
    shash = Binary(sha.new(secret).digest())
    response = None
    if secret == "":
        response = res[pxy.put(key,val, ttl, "put.py")]
    else:
        response = res[pxy.put_removable(key,val, "SHA",shash, ttl, "put.py")]
    return HttpResponse("added colors=red and the response is "+ response)
