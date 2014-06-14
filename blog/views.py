from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from blog.models import *

def blog(request):
    billets = Billet.objects.all()
    return render_to_response('blog/blog.html', {'billets' : billets})#, context_instance=RequestContext(request))

def billet(request,billet_id):
    billet = Billet.objects.get(pk=billet_id)
    return render_to_response('blog/billet.html', {'billet' : billet})#, context_instance=RequestContext(request))
