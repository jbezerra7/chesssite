from django.urls import path

from . import views
from .views import ChessGameView

app_name = "chess"

urlpatterns = [
    path("", ChessGameView.as_view(), name="chess"),
    path('make_move/', ChessGameView.make_move, name='make_move'),
    path('players/<str:player>/', views.PlayerView.as_view(), name='player'),
    path('profile/', views.SelfPlayerView, name='profile'),
]