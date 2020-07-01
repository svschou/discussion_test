from django.contrib import admin
from threads.models import Reaction, Response, Brainstorm, BrainstormResponse, BrainstormComment, Vote, Discussion, DiscussionReply

# Register your models here.
admin.site.register(Reaction)
admin.site.register(Response)
admin.site.register(Brainstorm)
admin.site.register(BrainstormResponse)
admin.site.register(BrainstormComment)
admin.site.register(Vote)
admin.site.register(Discussion)
admin.site.register(DiscussionReply)
