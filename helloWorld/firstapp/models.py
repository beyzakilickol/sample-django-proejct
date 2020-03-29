from django.db import models
# django has already a User model
from django.contrib.auth.models import User

# Create your models here.



GAME_STATUS_CHOICES = (
    ('F', 'First Player To Move'),
    ('S', 'Second Player To Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second PLayer Wins'),
    ('D', 'Draw')
)

class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)
    # auto_now will update every time you save the model.
    # auto_now_add is set only on create
    # If you use auto_now_add then you cannot set the field on your model manually.
    start_time = models.DateTimeField(auto_now=True)
    last_active = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    def __str__(self):
        return f"{self.first_player} vs {self.second_player}"

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    content = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)





