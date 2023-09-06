from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django_filters.views import FilterView
from cricket_app.filters import TeamFilter, PlayerFilter, SquadFilter, MatchFilter
from cricket_app.forms import TeamForm, PlayerForm, SquadForm, MatchForm
from cricket_app.models import Team, Player, Squad, Match


class Index(TemplateView):
    template_name = 'index.html'


class TeamCreateView(CreateView):
    form_class = TeamForm
    template_name = 'team/team_update.html'
    success_url = reverse_lazy('cricket_app:team_list')


class TeamListView(FilterView):
    template_name = 'team/team_list.html'
    context_object_name = 'teams'
    filterset_class = TeamFilter

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Team.objects.filter(Q(name__icontains=query))
        else:
            return Team.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        context['form'] = TeamForm
        return context


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'team/team_update.html'
    success_url = reverse_lazy('cricket_app:team_list')


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy('cricket_app:team_list')


class PlayerCreateView(CreateView):
    form_class = PlayerForm
    template_name = 'player/player_update.html'
    success_url = reverse_lazy('cricket_app:player_list')


class PlayerListView(FilterView):
    template_name = 'player/player_list.html'
    context_object_name = 'players'
    filterset_class = PlayerFilter

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Player.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) |
                                         Q(team__name__icontains=query))
        else:
            return Player.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        context['form'] = PlayerForm
        return context


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player/player_update.html'
    success_url = reverse_lazy('cricket_app:player_list')


class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('cricket_app:player_list')


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player/player_detail.html'
    context_object_name = 'player'


class SquadCreateView(CreateView):
    form_class = SquadForm
    template_name = 'squad/squad_create.html'
    success_url = reverse_lazy('cricket_app:squad_list')


class SquadListView(FilterView):
    model = Squad
    template_name = 'squad/squad_list.html'
    context_object_name = 'squads'
    filterset_class = SquadFilter

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Squad.objects.filter(Q(name__icontains=query) | Q(team__name__icontains=query))

        else:
            return Squad.objects.all()


class SquadUpdateView(UpdateView):
    model = Squad
    form_class = SquadForm
    template_name = 'squad/squad_create.html'
    success_url = reverse_lazy('cricket_app:squad_list')


class SquadDeleteView(DeleteView):
    model = Squad
    success_url = reverse_lazy('cricket_app:squad_list')


class SquadDetailView(DetailView):
    model = Squad
    template_name = 'squad/squad_detail.html'
    context_object_name = 'squad'


class MatchCreateView(CreateView):
    form_class = MatchForm
    template_name = 'match/match_create.html'
    success_url = reverse_lazy('cricket_app:match_list')


class MatchListView(FilterView):
    model = Match
    template_name = 'match/match_list.html'
    context_object_name = 'matches'
    filterset_class = MatchFilter

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Match.objects.filter(Q(squad_one__name__icontains=query) |
                                        Q(squad_two__name__icontains=query))

        else:
            return Match.objects.all()


class MatchUpdateView(UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'match/match_create.html'
    success_url = reverse_lazy('cricket_app:match_list')


class MatchDeleteView(DeleteView):
    model = Match
    success_url = reverse_lazy('cricket_app:match_list')


class MatchDetailView(DetailView):
    model = Match
    template_name = 'match/match_detail.html'
    context_object_name = 'match'
