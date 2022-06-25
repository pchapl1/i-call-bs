from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'), 

    # =============================CREATE=============================
    path('polls/new', CreatePollView.as_view(), name = 'create_poll'), 
    

    # =============================READ=============================
    path('polls/<pk>', DetailPollView.as_view(), name = 'read_poll'), 
    path('polls/all/<pk>', AllPollsView.as_view(), name = 'read_polls'), 
    path('polls/popular-today', PopularTodayView.as_view(), name = 'popular_today'), 
    path('rankings', RankingsView.as_view(), name = 'rankings'), 




    # =============================UPDATE=============================
    path('polls/edit/<pk>', EditPollView.as_view(), name = 'edit_poll'), 



    # =============================DELETE=============================
    path('polls/del/<pk>', views.del_poll, name = 'del_poll'), 




]