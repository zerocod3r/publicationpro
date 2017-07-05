from django.contrib import admin
from .models import *

admin.site.register(UserSignup)
admin.site.register(UserProfile)
admin.site.register(PubSignup)
admin.site.register(PublisherProfile)
admin.site.register(Manuscript)

