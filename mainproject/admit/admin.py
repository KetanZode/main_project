from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Prerequisite)
admin.site.register(MeansToApply)
admin.site.register(CourseCategory)