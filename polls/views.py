from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import User
import json

class HomeView(LoginRequiredMixin, ListView):
    model = Poll
    template_name = 'home.html'

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
            
class AboutView(TemplateView):   
    template_name = 'about.html'



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
            return initial
        except Exception as e:
            print(f'create poll error: {e}')


def create_vote(request):
    try:
        response_data = {}

        poll = Poll.objects.get(pk = 3)


        if request.method == 'POST':

            form_data = request.POST

            poll_id = form_data['the_poll']

            poll = Poll.objects.get(pk = poll_id)

            print(f'poll: {poll}')

            if form_data['vote'] == 'true':

                Vote.objects.create(is_bs = False, voted_on_by = request.user, poll = poll)

            else:
                Vote.objects.create(is_bs = True, voted_on_by = request.user, poll = poll)

            response_data['true_votes'] = len([x for x in poll.votes.all() if x.is_bs == False])
            response_data['bs_votes'] = len([x for x in poll.votes.all() if x.is_bs == True])
            response_data['poll_pk'] = poll.pk

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


class CategoryView(ListView):
    model = Poll
    template_name = 'polls/categories.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            politics_polls = Poll.objects.filter(category = 3)
            politics_bs = [len(Vote.objects.filter(poll=x, is_bs = True)) for x in politics_polls]
            politics_truth = [len(Vote.objects.filter(poll=x, is_bs = False)) for x in politics_polls]
            context['politics'] = zip(politics_polls,politics_bs,politics_truth)

            sports_polls = Poll.objects.filter(category = 1)
            sports_bs = [len(Vote.objects.filter(poll=x, is_bs = True)) for x in sports_polls]
            sports_truth = [len(Vote.objects.filter(poll=x, is_bs = False)) for x in sports_polls]
            context['sports'] = zip(sports_polls,sports_bs,sports_truth)


            history_polls = Poll.objects.filter(category = 2)
            history_bs = [len(Vote.objects.filter(poll=x, is_bs = True)) for x in history_polls]
            history_truth = [len(Vote.objects.filter(poll=x, is_bs = False)) for x in history_polls]
            context['history'] = zip(history_polls,history_bs,history_truth)

            science_polls = Poll.objects.filter(category = 4)
            science_bs = [len(Vote.objects.filter(poll=x, is_bs = True)) for x in science_polls]
            science_truth = [len(Vote.objects.filter(poll=x, is_bs = False)) for x in science_polls]
            context['science'] = zip(science_polls,science_bs,science_truth)


            return context
        except Exception as e:
            print(f'context error : {e}')

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