
#-----------defining chess pieces and the columns letters-----------#
white_pieces = {'wk': '♔', 'wq': '♕', 'wr': '♖', 'wb': '♗', 'wkn': '♘', 'wp': '♙'}
black_pieces = {'bp': '♟', 'bh': '♞', 'bb': '♝', 'br': '♜', 'bk': '♚', 'bq': '♛'}
columns = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']

#-----------defining the board with initial placement of pieces-----------#
board = [
        [black_pieces['br'],black_pieces['bh'],black_pieces['bb'],black_pieces['bq'],black_pieces['bk'],black_pieces['bb'],black_pieces['bh'],black_pieces['br']],
        [black_pieces['bp'],black_pieces['bp'],black_pieces['bp'],black_pieces['bp'],black_pieces['bp'],black_pieces['bp'],black_pieces['bp'],black_pieces['bp']],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        [white_pieces['wp'],white_pieces['wp'],white_pieces['wp'],white_pieces['wp'],white_pieces['wp'],white_pieces['wp'],white_pieces['wp'],white_pieces['wp']],
        [white_pieces['wr'],white_pieces['wkn'],white_pieces['wb'],white_pieces['wq'],white_pieces['wk'],white_pieces['wb'],white_pieces['wkn'],white_pieces['wr']],
        ]

#-----------drawing the board-----------#
def draw(board):
    global columns
    print(columns)
    for i in range(len(board)):
        print(board[i], i+1) #adding a number to indicate the rows 


#-----------the execution sequence-----------#
chess = True
while chess:

    draw(board)

    #takes piece and movement place from user
    piece_to_move = input('enter the piece: ')
    place_to_move = input('enter the place: ')

    #getting the index of both row and column of entered piece
    piece_row_index = int(piece_to_move[1]) - 1
    piece_column_index = columns.index(piece_to_move[0])

    #getting the index of both row and column of entered place
    place_row_index = int(place_to_move[1]) - 1
    place_column_index = columns.index(place_to_move[0])

    #moving the piece and clearing it's previous position
    board[place_row_index][place_column_index] = board[piece_row_index][piece_column_index]
    board[piece_row_index][piece_column_index] = '-'
 
    





