from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404

from models import User

def index(request):    
	"""
	The landing page
	"""
	rc = RequestContext(request)
	users = User.objects.all()
	rc['users'] = users
	return render_to_response('myapp/index.html', rc)

