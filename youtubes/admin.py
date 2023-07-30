from http.client import ImproperConnectionState
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Video , Comment

class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Video )
admin.site.register(Comment  )