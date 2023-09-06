import django_filters
from django import forms

from cricket_app.models import Team, Player, Squad, Match


class TeamFilter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(queryset=Team.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}))

    def __init__(self, *args, **kwargs):
        super(TeamFilter, self).__init__(*args, **kwargs)
        # for field in self.filters:
        #     self.filters[field].field.widget.attrs['class'] = 'form-control'
        # self.filters['name'].field.widget.attrs.update({'class': 'select2'})

    class Meta:
        model = Team
        fields = ['name']


class PlayerFilter(django_filters.FilterSet):
    format = django_filters.ChoiceFilter(choices=Player.FORMAT)
    type = django_filters.ChoiceFilter(choices=Player.TYPE)

    def __init__(self, *args, **kwargs):
        super(PlayerFilter, self).__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'format', 'type']


class SquadFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super(SquadFilter, self).__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Squad
        fields = ['name', 'team']


class MatchFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Match.STATUS)
    result = django_filters.ChoiceFilter(choices=Match.RESULT)
    type = django_filters.ChoiceFilter(choices=Match.TYPE)

    def __init__(self, *args, **kwargs):
        super(MatchFilter, self).__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Match
        fields = ['squad_one', 'squad_two', 'location', 'date', 'winner', 'status', 'result', 'type']
