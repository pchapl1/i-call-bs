from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Poll
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import User
import json

class HomeView(LoginRequiredMixin, ListView):
    model = Poll
    template_name = 'home.html'
class AboutView(TemplateView):   
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            polls = Poll.objects.all()
            bs = [len(Vote.objects.filter(poll=x, is_bs = True)) for x in polls]
            truth = [len(Vote.objects.filter(poll=x, is_bs = False)) for x in polls]
            context['polls'] = zip(polls,bs,truth)
            return context
        except Exception as e:
            print(f'context error : {e}')


    # =============================CREATE VIEWS=============================

class CreatePollView(CreateView):
    model = Poll
    template_name = 'polls/create_poll.html'
    form_class = PollForm

    def form_valid(self, form):
        try:
            form.instance.created_by = self.request.user
        except Exception as e:
            f"{e}"
        return super().form_valid(form)

    def get_initial(self):
        try:
            
            initial = super(CreatePollView, self).get_initial()
            initial['created_by'] = self.request.user
            print(initial['created_by'])
            return initial
        except Exception as e:
            print(f'create poll error: {e}')


def create_vote(request, pk):
    try:
        response_data = {}
        if request.method == 'POST':
            form_data = request.POST
            poll = Poll.objects.get(pk = pk)
            if form_data['is_bs'] == 'true':

                Vote.objects.create(is_bs = True, voted_on_by = request.user, poll = poll)
            else:
                Vote.objects.create(is_bs = False, voted_on_by = request.user, poll = poll)
            return HttpResponse(json.dumps(response_data), content_type='application.json')
    except Exception as e:
        print(f'create vote error: {e}')


    # =============================READ VIEWS=============================
class DetailPollView(DetailView):
    model = Poll
    template_name = 'polls/poll_detail.html'


# class AllPollsView(ListView):
#     model = Poll
#     template_name = 'home.html'
#     context_object_name = 'polls'


class PopularTodayView(ListView):
    model = Poll
    template_name = 'polls/popular_today.html'


class RankingsView(ListView):
    model = Poll
    template_name = 'polls/rankings.html'
    

    # =============================UPDATE VIEWS=============================
class EditPollView(UpdateView):
    model = Poll
    template_name = 'polls/update_poll.html'
    form_class = PollForm



# def poll_vote(request, pk):
#     poll = Poll.objects.get(id=pk)
#     vote = Vote.objects.create()


    # =============================DELETE VIEWS=============================

def del_poll(request, pk):
    try:
        poll = Poll.objects.get(pk = pk)
        poll.delete()
        return redirect(reverse('home'))
    except Exception as e:
        print(f'poll delete error : {e}')