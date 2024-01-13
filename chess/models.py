from django.db import models

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