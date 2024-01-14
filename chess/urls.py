from django.urls import path

from . import views
from .views import ChessGameView

urlpatterns = [
    path("", views.index, name="index"),
    path("chess", ChessGameView.as_view(), name="chess"),
    path('make_move/', ChessGameView.make_move, name='make_move'),

]