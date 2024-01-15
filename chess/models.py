from django.db import models
from django.conf import settings

COLOR_CHOICES = (
    ('white','WHITE'),
    ('black','BLACK'),
)

PIECE_CHOICES = (
    ('pawn','PAWN'),
    ('bishop','BISHOP'),
    ('knight','KNIGHT'),
    ('rook','ROOK'),
    ('queen','QUEEN'),
    ('king','KING'),
)

# Create your models here.
class Board(models.Model):
    id = models.BigIntegerField
    state = models.JSONField

class Move(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='moves')
    made = models.DateTimeField(auto_now_add=True)
    piece = models.CharField(max_length=6, choices=PIECE_CHOICES, default='pawn')
    color = models.CharField(max_length=5, choices=COLOR_CHOICES, default='white') #black will be true
    move = models.CharField(max_length=16)#example: b2 to b3

#we'll leave this multi-lobby system to later
class Lobby(models.Model):
    name = models.TextField()
    capacity = models.SmallIntegerField(default=6)
    lobby_name = models.SlugField(unique=True)

#if you check signals.py, this "Player" gets created in our chess app
#after an account is made with the django authentication app
#so we're extending the authentication model to have use in our app
class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='player', on_delete=models.CASCADE,)
    
    ingame = models.ForeignKey(Lobby, on_delete=models.SET_NULL, related_name='players', default="", null=True)
    #ingame field is a placeholder until Lobby model is being used
   
    player = models.CharField(max_length=16, default="")
    #player field because maybe users will want a seperate username and profile name
    
    wins = models.IntegerField()

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return self.user.username