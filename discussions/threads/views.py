from django.shortcuts import render
from threads.models import Reaction, Response
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from threads.forms import ResponseForm

# logging stuff ------------------------------------------------------------------------
import logging

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})

logger = logging.getLogger(__name__)
# -------------------
# ------------------------------------------------------------------------------------

# Create your views here.
class ReactListView(ListView):
	model = Reaction
	template_name = "threads/thread_list.html"

	def get(self, request) :
		r_list = Reaction.objects.all()
		ctx = {'r_list':r_list}
		#print(r_list[0])
		return render(request, self.template_name, ctx)

class ReactDetailView(DetailView):
	model = Reaction
	template_name = "threads/thread_detail.html"

	def get(self, request, pk) :
		react = Reaction.objects.get(id=pk)
		resps = Response.objects.filter(reaction=react)
		resp_form = ResponseForm()
		ctx = {'react':react, 'resps':resps, 'resp_form':resp_form}
		return render(request, self.template_name, ctx)

class ReactCreateView(CreateView):
	model = Reaction
	template_name = "threads/thread_form.html"
	fields = ['text', 'owner']
	success_url = reverse_lazy('threads:reactions')

class RespCreateView(View):
	model = Response
	def post(self, request, pk) :
		r = get_object_or_404(Reaction, id=pk)
		owner = get_object_or_404(User, id=request.POST['owner'])
		resp = Response(text=request.POST['text'], owner=owner, reaction=r)
		resp.save()
		return redirect(reverse('threads:reaction_detail', args=[pk]))
# ----------------------------------------------
from django.db import connection
print(connection.queries)

