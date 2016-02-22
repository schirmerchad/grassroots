#from django.shortcuts import render
#
# # Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Voter

class IndexView(generic.DetailView):
    template_name = 'index.html'

class ProfileView(generic.DetailView):
    model = Voter
    template_name = 'profile.html'
