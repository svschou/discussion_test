from django.urls import path, reverse_lazy
from . import views

app_name='threads'
urlpatterns = [
	path('',
		views.PostsView.as_view(), name='all_posts'),
	path('posts/new',
		views.PostCreate.as_view(), name='new_post'),

	path('reactions',
		views.ReactListView.as_view(), name='reactions'),
	path('reaction/<int:pk>',
		views.ReactDetailView.as_view(), name='reaction_detail'),
	path('reaction/create',
		views.ReactCreateView.as_view(), name='reaction_create'),
	path('reaction/<int:pk>/resp',
        views.RespCreateView.as_view(), name='reaction_resp_create'),

	path('brainstorms',
		views.BrainListView.as_view(), name='brainstorms'),
	path('brainstorm/<int:pk>',
		views.BrainDetailView.as_view(), name='brainstorm_detail'),

	path('brainstorm/<int:pk>/addupvote', 
		views.AddUpvoteView.as_view(), name='brainstorm_add_upvote'),

	path('brainstorm/create',
		views.BrainCreateView.as_view(), name='brainstorm_create'),
	path('brainstorm/<int:pk>/resp',
		views.BrainRespCreateView.as_view(), name='brainstorm_resp_create'),
	path('brainstorm/<int:pk>/comment',
		views.BrainCommentCreateView.as_view(), name='brainstorm_comment_create'),

	path('discussions',
		views.DiscListView.as_view(), name='discussions'),
	path('discussion/<int:pk>',
		views.DiscDetailView.as_view(), name='discussion_detail'),
	path('discussion/create',
		views.DiscCreateView.as_view(), name='discussion_create'),
	path('discussion/<int:pk>/reply',
        views.ReplyCreateView.as_view(), name='discussion_reply_create'),
]