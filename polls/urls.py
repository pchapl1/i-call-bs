from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'), 
    path('about/', AboutView.as_view(), name = 'about'),

    # =============================CREATE=============================
    path('new-poll', CreatePollView.as_view(), name = 'create_poll'), 
    path('new-vote/<int:pk>', views.create_vote, name = 'create_vote'), 
    

    # =============================READ=============================
    path('<int:pk>', DetailPollView.as_view(), name = 'read_poll'), 
    # path('all/<int:pk>', AllPollsView.as_view(), name = 'read_polls'), 
    path('popular-today', PopularTodayView.as_view(), name = 'popular_today'), 
    path('rankings', RankingsView.as_view(), name = 'rankings'), 




    # =============================UPDATE=============================
    path('edit-poll/<pk>', EditPollView.as_view(), name = 'edit_poll'), 
    # path('vote/<pk>', views.poll_vote, name = 'poll_vote'), 



    # =============================DELETE=============================
    path('del-poll/<pk>', views.del_poll, name = 'del_poll'), 




]