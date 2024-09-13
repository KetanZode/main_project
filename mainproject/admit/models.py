from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    daad_url = models.URLField(max_length=300, null=True, blank=True)
    official_url = models.URLField(max_length=300, null=True, blank=True)
    additional_url = models.URLField(max_length=500, null=True, blank=True)
    courses = models.ManyToManyField('Course', related_name='universities', null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    form_in = models.BooleanField(null=True, blank=True)
    prerequisites = models.ManyToManyField('Prerequisite', related_name='courses', null=True, blank=True)
    prereq_completed = models.BooleanField(default=False, null=True, blank=True)
    applied = models.BooleanField(default=False, null=True, blank=True)
    result_in = models.BooleanField(default=False,null=True, blank=True)
    admitted = models.BooleanField(null=True, blank=True)
    means_to_apply = models.ForeignKey('MeansToApply', related_name='courses', on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    additional_url = models.URLField(max_length=500, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

class Prerequisite(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    additional_url = models.URLField(max_length=500, null=True, blank=True)

class MeansToApply(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    additional_url = models.URLField(max_length=500,null=True, blank=True)