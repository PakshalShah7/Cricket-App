from django.forms import ModelForm, ValidationError, DateInput
from cricket_app.models import Team, Player, Squad, Match


class TeamForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Team
        fields = ['name', 'logo']

    def clean(self):
        cleaned_data = super(TeamForm, self).clean()
        name = self.cleaned_data.get('name')

        if Team.objects.filter(name=name).exists():
            return ValidationError("Team name is already exists")

        return cleaned_data


class PlayerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['team'].widget.attrs['class'] = 'select2 form-control'
        self.fields['format'].widget.attrs['class'] = 'select2 form-control'
        self.fields['type'].widget.attrs['class'] = 'select2 form-control'

    class Meta:
        model = Player
        fields = '__all__'


class SquadForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SquadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['team'].widget.attrs['class'] = 'select2 form-control'
        self.fields['players'].widget.attrs['class'] = 'select2 form-control'
        self.fields['captain'].widget.attrs['class'] = 'select2 form-control'
        self.fields['vice_captain'].widget.attrs['class'] = 'select2 form-control'
        self.fields['playing_eleven'].widget.attrs['class'] = 'select2 form-control'

    class Meta:
        model = Squad
        fields = '__all__'

    def clean(self):
        cleaned_data = super(SquadForm, self).clean()
        name = self.cleaned_data.get('name')
        team = self.cleaned_data.get('team')
        players = self.cleaned_data.get('players')
        captain = self.cleaned_data.get('captain')
        vice_captain = self.cleaned_data.get('vice_captain')
        playing_eleven = self.cleaned_data.get('playing_eleven')

        if Squad.objects.filter(name=name).exists():
            raise ValidationError("Squad name is already exists")
        if captain == vice_captain:
            raise ValidationError("Captain and Vice-captain should not be same.")
        for player in players:
            if player.team != team:
                raise ValidationError("Player should belong to the selected team")
        for player in playing_eleven:
            if player not in players:
                raise ValidationError("Players should be selected from the selected squad players")
        if captain and vice_captain not in playing_eleven:
            raise ValidationError("Both captain and vice_captain should be present in playing eleven")

        return cleaned_data


class MatchForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        DateInput.input_type = "date"
        self.fields['team_one'].widget.attrs['class'] = 'select2 form-control'
        self.fields['team_two'].widget.attrs['class'] = 'select2 form-control'
        self.fields['squad_one'].widget.attrs['class'] = 'select2 form-control'
        self.fields['squad_two'].widget.attrs['class'] = 'select2 form-control'
        self.fields['toss'].widget.attrs['class'] = 'select2 form-control'
        self.fields['winner'].widget.attrs['class'] = 'select2 form-control'
        self.fields['status'].widget.attrs['class'] = 'select2 form-control'
        self.fields['result'].widget.attrs['class'] = 'select2 form-control'
        self.fields['type'].widget.attrs['class'] = 'select2 form-control'

    class Meta:
        model = Match
        fields = '__all__'

    def clean(self):
        cleaned_data = super(MatchForm, self).clean()
        team_one = self.cleaned_data.get('team_one')
        team_two = self.cleaned_data.get('team_two')
        squad_one = self.cleaned_data.get('squad_one')
        squad_two = self.cleaned_data.get('squad_two')
        toss = self.cleaned_data.get('toss')
        winner = self.cleaned_data.get('winner')

        if team_one == team_two:
            raise ValidationError("Both teams should not be same")
        if squad_one == squad_two:
            raise ValidationError("Both squads should not be same")
        if toss != team_one or toss != team_two:
            raise ValidationError("Toss should be won only by either of both teams")
        if winner != team_one or winner != team_two:
            raise ValidationError("Winner should be only by either of both teams")

        return cleaned_data
