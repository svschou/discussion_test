from django.shortcuts import render
from threads.models import Reaction, Response, Brainstorm, BrainstormResponse, BrainstormComment, Vote, Discussion, DiscussionReply
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from threads.forms import ResponseForm, BrainResponseForm, BrainCommentForm, ReplyForm, ReactForm
from django.contrib.auth.mixins import LoginRequiredMixin


# dj4e-samples/favsql/sqldebug.py
from django.db import connection
def print_queries():
    retval = list()
    for i, query in enumerate(connection.queries):
        q = query['sql']
        if q.find('SELECT "django_session"."session_key"') == 0 : continue
        if q.find('SELECT "auth_user"."id", "auth_user"."password"') == 0 : continue
        print(q)

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

# ------------------------------------------------------------------------------------
import operator

class PostsView(ListView):
	template_name = "threads/all_posts.html"

	def get(self, request) :
		all_posts = []
		models = {Reaction:('reaction', 'lightseagreen'), 
				  Brainstorm:('brainstorm','mediumpurple'), 
				  Discussion:('discussion','lightcoral')}
		for model in models:
			posts = model.objects.all()
			for p in posts:
				p.type = models[model][0]
				p.color = models[model][1]
			all_posts.extend(posts)

		all_posts = sorted(all_posts, key=operator.attrgetter('created_at'))
		#all_posts.append(Reaction.objects.all())
		#model = Brainstorm
		#all_posts.append(Brainstorm.objects.all())
		#model = Discussion
		#all_posts.append(Discussion.objects.all())
		print(all_posts)
		ctx = {'all_posts':all_posts}
		print_queries()
		return render(request, self.template_name, ctx)

class PostCreate(View):
	template_name = "threads/new_post.html"
	def get(self, request) :
		return render(request, self.template_name)


# ------------------------------------------------------------------------------------

class ReactListView(ListView):
	model = Reaction
	template_name = "threads/thread_list.html"

	def get(self, request) :
		r_list = Reaction.objects.all()
		ctx = {'r_list':r_list}
		#print(r_list[0])
		print_queries()
		return render(request, self.template_name, ctx)

class ReactDetailView(DetailView):
	model = Reaction
	template_name = "threads/thread_detail.html"

	def get(self, request, pk) :
		react = Reaction.objects.get(id=pk)
		resps = Response.objects.filter(reaction=react)
		resp_form = ResponseForm()
		ctx = {'react':react, 'resps':resps, 'resp_form':resp_form}
		print_queries()
		return render(request, self.template_name, ctx)

class ReactCreateView(View):
	def get(self, request):
		model = Reaction
		template_name = "threads/thread_form.html"
		fields = ['topic', 'text', 'owner']
		success_url = reverse_lazy('threads:all_posts')
		form = ReactForm
		ctx = {''}

	def post(self, request, pk) :
		owner = get_object_or_404(User, id=request.POST['owner'])
		react = Reaction(topic=request.POST['topic'], text=request.POST['text'], owner=owner)
		react.save()
		return redirect(reverse('threads:reaction_detail', args=[pk.id]))


	# def get(self, request):
	# 	model = Reaction
	# 	template_name = "threads/thread_form.html"
	# 	fields = ['topic', 'text', 'owner']
		#success_url = reverse_lazy('threads:all_posts')
		#return redirect(reverse('threads:reaction_detail', args=[1]))
		#return redirect(reverse('threads:all_posts'))

class RespCreateView(View):
	model = Response
	def post(self, request, pk) :
		r = get_object_or_404(Reaction, id=pk)
		owner = get_object_or_404(User, id=request.POST['owner'])
		resp = Response(text=request.POST['text'], owner=owner, reaction=r)
		resp.save()
		print_queries()
		return redirect(reverse('threads:reaction_detail', args=[pk]))

# ------------------------------------------------------------------------------------

class BrainListView(ListView):
	model = Brainstorm
	template_name = 'threads/brain_list.html'

	def get(self, request) :
		b_list = Brainstorm.objects.all()
		ctx = {'b_list':b_list}
		#print(b_list[0])
		print_queries()
		return render(request, self.template_name, ctx)

class BrainDetailView(DetailView):
	model = BrainstormResponse
	template_name = "threads/brain_detail.html"

	def get(self, request, pk) :
		brain = Brainstorm.objects.get(id=pk)
		brain_resps = BrainstormResponse.objects.filter(brainstorm=brain)
		#brain.votes = []
		#brain.comments = []
		brain.resps = []
		for resp in brain_resps:
			r = resp
			r.r_votes = Vote.objects.filter(brainresponse=resp)
			r.up_votes = Vote.objects.filter(brainresponse=resp, direction='u')
			r.down_votes = Vote.objects.filter(brainresponse=resp, direction='d')

			r.r_comments = BrainstormComment.objects.filter(brainstormresponse=resp)
			r.up = len(r.up_votes)
			r.down = len(r.down_votes)
			r.net = r.up - r.down
			r.num_votes = len(r.r_votes)
			brain.resps.append(r)
		brain.resps = sorted(brain.resps, key=operator.attrgetter('net'), reverse=True)
		#brain.num_votes = len(brain.votes)

		resp_form = BrainResponseForm()
		comment_form = BrainCommentForm()
		ctx = {'brain':brain, 'resp_form':resp_form, 'comment_form':comment_form}
		#ctx = {'brain':brain, 'brain_resps':resps, 'resp_form':resp_form}#, 'votes':votes, 'comments':comments}
		print_queries()

		return render(request, self.template_name, ctx)

class BrainCreateView(CreateView):
#class ReactCreateView(CreateView):
	model = Brainstorm
	template_name = "threads/brain_form.html"
	fields = ['topic', 'text', 'owner']
	success_url = reverse_lazy('threads:brainstorm_detail')
	print_queries()

class BrainRespCreateView(View):
	model = BrainstormResponse
	def post(self, request, pk) :
		b = get_object_or_404(Brainstorm, id=pk)
		owner = get_object_or_404(User, id=request.POST['owner'])
		resp = BrainstormResponse(text=request.POST['text'], owner=owner, brainstorm=b)
		resp.save()
		print_queries()
		return redirect(reverse('threads:brainstorm_detail', args=[pk]))

class BrainCommentCreateView(View): # FIX THIS
	model = BrainstormComment
	def post(self, request, pk) :
		b = get_object_or_404(BrainstormResponse, id=pk)
		owner = get_object_or_404(User, id=request.POST['owner'])
		comment = BrainstormComment(text=request.POST['text'], owner=owner, brainstormresponse=b)
		comment.save()
		return redirect(reverse('threads:brainstorm_detail', args=[pk]))

# ------------------------------------------------------------------------------------

class DiscListView(ListView):
	model = Discussion
	template_name = 'threads/disc_list.html'

	def get(self, request) :
		d_list = Discussion.objects.all()
		ctx = {'d_list':d_list}
		#print(b_list[0])
		print_queries()
		return render(request, self.template_name, ctx)

class DiscDetailView(DetailView):
	model = Discussion
	template_name = "threads/disc_detail.html"

	def get(self, request, pk) :
		disc = Discussion.objects.get(id=pk)
		replies = DiscussionReply.objects.filter(discussion=disc)
		reply_form = ReplyForm()
		ctx = {'disc':disc, 'replies':replies, 'reply_form':reply_form}
		print_queries()
		return render(request, self.template_name, ctx)

class DiscCreateView(CreateView): # change to pass new id to discussion detail
#class ReactCreateView(CreateView):
	model = Discussion
	template_name = "threads/disc_form.html"
	fields = ['topic', 'text', 'owner']
	success_url = reverse_lazy('threads:all_posts')
	print_queries()

class ReplyCreateView(View):
	model = DiscussionReply
	def post(self, request, pk) :
		d = get_object_or_404(Discussion, id=pk)
		owner = get_object_or_404(User, id=request.POST['owner'])
		reply = DiscussionReply(text=request.POST['text'], owner=owner, discussion=d)
		reply.save()
		print_queries()
		return redirect(reverse('threads:discussion_detail', args=[pk]))





