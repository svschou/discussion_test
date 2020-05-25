from django.urls import path, reverse_lazy
from . import views

app_name='threads'
urlpatterns = [
	path('',
		views.ReactListView.as_view(), name='reactions'),
	path('reaction/<int:pk>',
		views.ReactDetailView.as_view(), name='reaction_detail'),
	path('reaction/create',
		views.ReactCreateView.as_view(), name='reaction_create'),
	path('reaction/<int:pk>/resp',
        views.RespCreateView.as_view(), name='reaction_resp_create'),
]