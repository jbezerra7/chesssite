import json
from urllib import request
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ChessGameView(View):
    board_state = {}

    #Dictionary mapping chess key to unicode character
    pieces = {
        'K': '\u2654', 'Q': '\u2655', 'R': '\u2656',
        'B': '\u2657', 'N': '\u2658', 'P': '\u2659',
        'k': '\u265A', 'q': '\u265B', 'r': '\u265C',
        'b': '\u265D', 'n': '\u265E', 'p': '\u265F'
    }

    def get(self, request, *args, **kwargs):
        #Update to check is game is active or new
        gameIsNew = True

        if(gameIsNew):
            board = self.initialize_board()
        else:
            #Define a finction to return the current active game
            board = ''
        
        # Pass the chess board to the template
        context = {'chess_board': board, 'board_structure': self.determine_board_structure(board)}
        return render(request, 'chess_board.html', context)

    def post(self, request, *args, **kwargs):
        # Logic to handle a move
        pass

    def initialize_board(self):
        # Initialize an empty chess board as a dictionary
        board_state = {i: '' for i in range(1, 65)}
        
        # Mapping the pieces to their starting positions
        # Pawns
        for i in range(8, 16):
            board_state[i + 1] = pieces['P']  # Black pawns
            board_state[64 - i] = pieces['p']  # White pawns
        
        # Rooks
        board_state[1], board_state[8] = pieces['R'], pieces['R']
        board_state[57], board_state[64] = pieces['r'], pieces['r']
        
        # Knights
        board_state[2], board_state[7] = pieces['N'], pieces['N']
        board_state[58], board_state[63] = pieces['n'], pieces['n']
        
        # Bishops
        board_state[3], board_state[6] = pieces['B'], pieces['B']
        board_state[59], board_state[62] = pieces['b'], pieces['b']
        
        # Queens and Kings
        board_state[4], board_state[5] = pieces['Q'], pieces['K']
        board_state[60], board_state[61] = pieces['q'], pieces['k']
        return board_state

    def determine_board_structure(self, board):
        board_structure = []
        for i in range(1, 65):
            row = (i - 1) // 8
            col = (i - 1) % 8
            square_color = 'dark' if (row + col) % 2 else 'light'
            board_structure.append({'index': i, 'color': square_color, 'piece': board.get(i, '&nbsp;')})
        return board_structure
    
    @require_http_methods(["POST"])
    @csrf_exempt
    def make_move(request):
        
        try:
            data = json.loads(request.body)
            print(data)
        except json.JSONDecodeError:
            print("Response is not in JSON format")

        # Logic to update the chess board
        # updated_board = your_function_to_update_board(from_square, to_square)

        return JsonResponse({'status': 'success', 'new_board_state': ''})
    
    def isLegalMove(self, startingIndex, endingIndex):
        match(self.board_state[startingIndex]):
            case 'p':
                return self.isLegalPawnMove(startingIndex, endingIndex)
            
    def isLegalPawnMove(self, startingIndex, endingIndex):
        legal = True
        moveStaysInSameCollumn = startingIndex - endingIndex % 8 != 0
        noPieceBlockingPath = self.board_state[startingIndex + 8] == ''
        capturingDiagonally = self.board_state[endingIndex] != ''  and startingIndex - endingIndex % 8 == 1
        if(moveStaysInSameCollumn):
            if(noPieceBlockingPath):
                legal = True
            else:
                legal = False
        elif(capturingDiagonally):
            legal = True
        else:
            legal = False
