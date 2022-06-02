import pygame
pygame.font.init()

# WINDOW
WIDTH, HEIGHT = 420, 420
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
FONT = pygame.font.SysFont('comicsans', 80)

FPS = 60

BG = (200, 255, 255) # background
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Board():
    def __init__(self, width, height):
        self.total = 0
        # BOARD LINES
        self.hor1 = pygame.Rect(0, height//3 -5, width, 10)
        self.hor2 = pygame.Rect(0, height//3 *2 -5, width, 10)
        self.ver1 = pygame.Rect(width//3 -5, 0, 10, height)
        self.ver2 = pygame.Rect(width//3 *2 -5, 0, 10, height)

        # ROW 1 BOXES
        self.box11 = Box(pygame.Rect(0, 0, width//3 -5, height//3 -5))
        self.box12 = Box(pygame.Rect(width//3 +5, 0, width//3 -10, height//3 -5))
        self.box13 = Box(pygame.Rect(width//3 *2 +5, 0, width//3 -5, height//3 -5))
        
        # ROW 2 BOXES
        self.box21 = Box(pygame.Rect(0, height//3 +5, width//3 -5, height//3 -10))
        self.box22 = Box(pygame.Rect(width//3 +5, height//3 +5, width//3 -10, height//3 -10))
        self.box23 = Box(pygame.Rect(width//3 *2 +5, height//3 +5, width//3 -5, height//3 -10))

        # ROW 3 BOXES
        self.box31 = Box(pygame.Rect(0, height//3 *2 +5, width//3 -5, height//3 -5))
        self.box32 = Box(pygame.Rect(width//3 +5, height//3 *2 +5, width//3 -10, height//3 -5))
        self.box33 = Box(pygame.Rect(width//3 *2 +5, height//3 * 2 +5, width//3 -5, height//3 -5))

        # WINNING X LINE COUNTS
        self.row1_x = 0
        self.row2_x = 0
        self.row3_x = 0
        self.col1_x = 0
        self.col2_x = 0
        self.col3_x = 0
        self.diag1_x = 0
        self.diag2_x = 0

        # WINNING O LINE COUNTS
        self.row1_o = 0
        self.row2_o = 0
        self.row3_o = 0
        self.col1_o = 0
        self.col2_o = 0
        self.col3_o = 0
        self.diag1_o = 0
        self.diag2_o = 0

class Box():
    def __init__(self, rect, contents=''):
        self.rect = rect
        self.contents = contents # ''=empty, 'X', 'O'
    
    def fill(self, contents):
        self.contents = contents

def draw_window(board):
    WIN.fill(BG)
    draw_board(board)
    draw_boxes(board)
    pygame.display.update()

def draw_board(board):
    # BOARD LINES
    pygame.draw.rect(WIN, BLACK, board.hor1)
    pygame.draw.rect(WIN, BLACK, board.hor2)
    pygame.draw.rect(WIN, BLACK, board.ver1)
    pygame.draw.rect(WIN, BLACK, board.ver2)
    
    # ROW 1 BOXES
    pygame.draw.rect(WIN, BG, board.box11.rect)
    pygame.draw.rect(WIN, BG, board.box12.rect)
    pygame.draw.rect(WIN, BG, board.box13.rect)

    # ROW 2 BOXES
    pygame.draw.rect(WIN, BG, board.box21.rect)
    pygame.draw.rect(WIN, BG, board.box22.rect)
    pygame.draw.rect(WIN, BG, board.box23.rect)

    # ROW 3 BOXES
    pygame.draw.rect(WIN, BG, board.box31.rect)
    pygame.draw.rect(WIN, BG, board.box32.rect)
    pygame.draw.rect(WIN, BG, board.box33.rect)

def draw_boxes(board):
    # ROW 1 BOXES
    WIN.blit(FONT.render(board.box11.contents, 1, BLACK), (35, 15))
    WIN.blit(FONT.render(board.box12.contents, 1, BLACK), (180, 15))
    WIN.blit(FONT.render(board.box13.contents, 1, BLACK), (320, 15))

    # ROW 2 BOXES
    WIN.blit(FONT.render(board.box21.contents, 1, BLACK), (35, 150))
    WIN.blit(FONT.render(board.box22.contents, 1, BLACK), (180, 150))
    WIN.blit(FONT.render(board.box23.contents, 1, BLACK), (320, 150))

    # ROW 3 BOXES
    WIN.blit(FONT.render(board.box31.contents, 1, BLACK), (35, 290))
    WIN.blit(FONT.render(board.box32.contents, 1, BLACK), (180, 290))
    WIN.blit(FONT.render(board.box33.contents, 1, BLACK), (320, 290))

def draw_winner(board):
    # X WINS
    if board.row1_x >= 3:
        WIN.blit(FONT.render(board.box11.contents, 1, RED), (35, 15))
        WIN.blit(FONT.render(board.box12.contents, 1, RED), (180, 15))
        WIN.blit(FONT.render(board.box13.contents, 1, RED), (320, 15))
    if board.row2_x >= 3:
        WIN.blit(FONT.render(board.box21.contents, 1, RED), (35, 150))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box23.contents, 1, RED), (320, 150))
    if board.row3_x >= 3:
        WIN.blit(FONT.render(board.box31.contents, 1, RED), (35, 290))
        WIN.blit(FONT.render(board.box32.contents, 1, RED), (180, 290))
        WIN.blit(FONT.render(board.box33.contents, 1, RED), (320, 290))
    if board.col1_x >= 3:
        WIN.blit(FONT.render(board.box11.contents, 1, RED), (35, 15))
        WIN.blit(FONT.render(board.box21.contents, 1, RED), (35, 150))
        WIN.blit(FONT.render(board.box31.contents, 1, RED), (35, 290))
    if board.col2_x >= 3:
        WIN.blit(FONT.render(board.box12.contents, 1, RED), (180, 15))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box32.contents, 1, RED), (180, 290))
    if board.col3_x >= 3:
        WIN.blit(FONT.render(board.box13.contents, 1, RED), (320, 15))
        WIN.blit(FONT.render(board.box23.contents, 1, RED), (320, 150))
        WIN.blit(FONT.render(board.box33.contents, 1, RED), (320, 290))
    if board.diag1_x >= 3:
        WIN.blit(FONT.render(board.box11.contents, 1, RED), (35, 15))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box33.contents, 1, RED), (320, 290))
    if board.diag2_x >= 3:
        WIN.blit(FONT.render(board.box13.contents, 1, RED), (320, 15))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box31.contents, 1, RED), (35, 290))
    
    # O WINS
    if board.row1_o >= 3:
        WIN.blit(FONT.render(board.box11.contents, 1, RED), (35, 15))
        WIN.blit(FONT.render(board.box12.contents, 1, RED), (180, 15))
        WIN.blit(FONT.render(board.box13.contents, 1, RED), (320, 15))
    if board.row2_o >= 3:
        WIN.blit(FONT.render(board.box21.contents, 1, RED), (35, 150))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box23.contents, 1, RED), (320, 150))
    if board.row3_o >= 3:
        WIN.blit(FONT.render(board.box31.contents, 1, RED), (35, 290))
        WIN.blit(FONT.render(board.box32.contents, 1, RED), (180, 290))
        WIN.blit(FONT.render(board.box33.contents, 1, RED), (320, 290))
    if board.col1_o >= 3:
        WIN.blit(FONT.render(board.box11.contents, 1, RED), (35, 15))
        WIN.blit(FONT.render(board.box21.contents, 1, RED), (35, 150))
        WIN.blit(FONT.render(board.box31.contents, 1, RED), (35, 290))
    if board.col2_o >= 3:
        WIN.blit(FONT.render(board.box12.contents, 1, RED), (180, 15))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box32.contents, 1, RED), (180, 290))
    if board.col3_o >= 3:
        WIN.blit(FONT.render(board.box13.contents, 1, RED), (320, 15))
        WIN.blit(FONT.render(board.box23.contents, 1, RED), (320, 150))
        WIN.blit(FONT.render(board.box33.contents, 1, RED), (320, 290))
    if board.diag1_o >= 3:
        WIN.blit(FONT.render(board.box11.contents, 1, RED), (35, 15))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box33.contents, 1, RED), (320, 290))
    if board.diag2_o >= 3:
        WIN.blit(FONT.render(board.box13.contents, 1, RED), (320, 15))
        WIN.blit(FONT.render(board.box22.contents, 1, RED), (180, 150))
        WIN.blit(FONT.render(board.box31.contents, 1, RED), (35, 290))

    pygame.display.update()
    pygame.time.delay(5000)

def handle_mouse_click(board, turn):
    if board.box11.rect.collidepoint(pygame.mouse.get_pos()): # box 11
        if board.box11.contents == '':
            board.box11.fill(turn)
            if (turn == 'X'):
                board.row1_x += 1
                board.col1_x += 1
                board.diag1_x += 1
            elif (turn == 'O'):
                board.row1_o += 1
                board.col1_o += 1
                board.diag1_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box12.rect.collidepoint(pygame.mouse.get_pos()): # box 12
        if board.box12.contents == '':
            board.box12.fill(turn)
            if (turn == 'X'):
                board.row1_x += 1
                board.col2_x += 1
            elif (turn == 'O'):
                board.row1_o += 1
                board.col2_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box13.rect.collidepoint(pygame.mouse.get_pos()): # box 13
        if board.box13.contents == '':
            board.box13.fill(turn)
            if (turn == 'X'):
                board.row1_x += 1
                board.col3_x += 1
                board.diag2_x += 1
            elif (turn == 'O'):
                board.row1_o += 1
                board.col3_o += 1
                board.diag2_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box21.rect.collidepoint(pygame.mouse.get_pos()): # box 21
        if board.box21.contents == '':
            board.box21.fill(turn)
            if (turn == 'X'):
                board.row2_x += 1
                board.col1_x += 1
            elif (turn == 'O'):
                board.row2_o += 1
                board.col1_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box22.rect.collidepoint(pygame.mouse.get_pos()): # box 22
        if board.box22.contents == '':
            board.box22.fill(turn)
            if (turn == 'X'):
                board.row2_x += 1
                board.col2_x += 1
                board.diag1_x += 1
                board.diag2_x += 1
            elif (turn == 'O'):
                board.row2_o += 1
                board.col2_o += 1
                board.diag1_o += 1
                board.diag2_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box23.rect.collidepoint(pygame.mouse.get_pos()): # box 23
        if board.box23.contents == '':
            board.box23.fill(turn)
            if (turn == 'X'):
                board.row2_x += 1
                board.col3_x += 1
            elif (turn == 'O'):
                board.row2_o += 1
                board.col3_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box31.rect.collidepoint(pygame.mouse.get_pos()): # box 31
        if board.box31.contents == '':
            board.box31.fill(turn)
            if (turn == 'X'):
                board.row3_x += 1
                board.col1_x += 1
                board.diag2_x += 1
            elif (turn == 'O'):
                board.row3_o += 1
                board.col1_o += 1
                board.diag2_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box32.rect.collidepoint(pygame.mouse.get_pos()): # box 32
        if board.box32.contents == '':
            board.box32.fill(turn)
            if (turn == 'X'):
                board.row3_x += 1
                board.col2_x += 1
            elif (turn == 'O'):
                board.row3_o += 1
                board.col2_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    elif board.box33.rect.collidepoint(pygame.mouse.get_pos()): # box 33
        if board.box33.contents == '':
            board.box33.fill(turn)
            if (turn == 'X'):
                board.row3_x += 1
                board.col3_x += 1
                board.diag1_x += 1
            elif (turn == 'O'):
                board.row3_o += 1
                board.col3_o += 1
                board.diag1_o += 1
            board.total += 1
            return change_turn(turn)
        else:
            return turn
    else:
        return turn

def change_turn(turn):
    if turn == 'X':
        return 'O'
    elif turn == 'O':
        return 'X'

def check_line(board):
    # X WINS
    if board.row1_x >= 3 or board.row2_x >= 3 or board.row3_x >= 3:
        return 'X'
    elif board.col1_x >= 3 or board.col2_x >= 3 or board.col3_x >= 3:
        return 'X'
    elif board.diag1_x >= 3 or board.diag2_x >= 3:
        return 'X'
    # O WINS
    if board.row1_o >= 3 or board.row2_o >= 3 or board.row3_o >= 3:
        return 'O'
    elif board.col1_o >= 3 or board.col2_o >= 3 or board.col3_o >= 3:
        return 'O'
    elif board.diag1_o >= 3 or board.diag2_o >= 3:
        return 'O'
    else:
        return ''

def main():
    board = Board(WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    run = True
    turn = 'X' # X goes first

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit game
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP: # mouse clicked
                turn = handle_mouse_click(board, turn)

        draw_window(board)
        winner = check_line(board)
        if winner != '' or board.total >= 9: # someone wins or tie
            draw_winner(board)
            break
    
    main()

if __name__ == '__main__':
    main()