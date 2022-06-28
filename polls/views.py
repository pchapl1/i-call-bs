from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import User

class HomeView(LoginRequiredMixin, ListView):
    model = Poll
    template_name = 'home.html'
    context_object_name = 'polls'




    # =============================CREATE VIEWS=============================

class CreatePollView(CreateView):
    model = Poll
    template_name = 'polls/create_poll.html'
    form_class = PollForm

    def form_valid(self, form):
        try:
            print('here')
            print( form.instance.created_by )
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

    # =============================DELETE VIEWS=============================

def del_poll(request, pk):
    try:
        poll = Poll.objects.get(pk = pk)
        poll.delete()
        return redirect(reverse('home'))
    except Exception as e:
       print(f'poll delete error : {e}')