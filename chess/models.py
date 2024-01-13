from django.db import models

# Create your models here.
class Board(models.Model):
    id = models.BigIntegerField
    state = models.JSONField

class History(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
