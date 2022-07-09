from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Poll
from django.urls import reverse_lazy
from .forms import PollForm
from django.db.models import Count

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
class AboutView(TemplateView):   
    template_name = 'about.html'

    # =============================CREATE VIEWS=============================

class CreatePollView(CreateView):
    model = Poll
    template_name = 'polls/create_poll.html'
    form_class = PollForm

    # =============================READ VIEWS=============================
class DetailPollView(DetailView):
    model = Poll
    template_name = 'polls/poll_detail.html'


class AllPollsView(ListView):
    model = Poll
    template_name = 'polls/all_polls.html'


class PopularTodayView(ListView):
    model = Poll
    template_name = 'polls/popular_today.html'


class RankingsView(ListView):
    model = Poll
    template_name = 'polls/rankings.html'
    dislikes = Poll.objects.annotate(count_dislikes=Count('dislikes')).order_by('count_dislikes')

    # =============================UPDATE VIEWS=============================
class EditPollView(UpdateView):
    model = Poll
    template_name = 'polls/update_poll.html'
    form_class = PollForm

    # =============================DELETE VIEWS=============================

def del_poll(request, pk):
    try:
        poll = Poll.objects.get(pk = pk)
        poll.delete()
        return redirect(reverse('home'))
    except Exception as e:
        print(f'poll delete error : {e}')