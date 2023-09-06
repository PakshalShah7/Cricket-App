from django.urls import path
from cricket_app.views import Index, TeamCreateView, TeamListView, TeamUpdateView, TeamDeleteView, \
    PlayerCreateView, PlayerUpdateView, PlayerListView, PlayerDeleteView, PlayerDetailView, SquadCreateView, \
    SquadListView, SquadUpdateView, SquadDeleteView, MatchCreateView, MatchListView, MatchUpdateView, MatchDeleteView, \
    MatchDetailView, SquadDetailView

app_name = 'cricket_app'

urlpatterns = [

    path('index/', Index.as_view(), name='index'),
    path('team/create/', TeamCreateView.as_view(), name='team_create'),
    path('team/list/', TeamListView.as_view(), name='team_list'),
    path('team/update/<int:pk>/', TeamUpdateView.as_view(), name='team_update'),
    path('team/delete/<int:pk>/', TeamDeleteView.as_view(), name='team_delete'),

    path('player/create/', PlayerCreateView.as_view(), name='player_create'),
    path('player/list/', PlayerListView.as_view(), name='player_list'),
    path('player/update/<int:pk>/', PlayerUpdateView.as_view(), name='player_update'),
    path('player/delete/<int:pk>/', PlayerDeleteView.as_view(), name='player_delete'),
    path('player/detail/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),

    path('squad/create/', SquadCreateView.as_view(), name='squad_create'),
    path('squad/list/', SquadListView.as_view(), name='squad_list'),
    path('squad/update/<int:pk>', SquadUpdateView.as_view(), name='squad_update'),
    path('squad/delete/<int:pk>', SquadDeleteView.as_view(), name='squad_delete'),
    path('squad/detail/<int:pk>', SquadDetailView.as_view(), name='squad_detail'),

    path('match/create/', MatchCreateView.as_view(), name='match_create'),
    path('match/list/', MatchListView.as_view(), name='match_list'),
    path('match/update/<int:pk>', MatchUpdateView.as_view(), name='match_update'),
    path('match/delete/<int:pk>', MatchDeleteView.as_view(), name='match_delete'),
    path('match/detail/<int:pk>', MatchDetailView.as_view(), name='match_detail'),

]
