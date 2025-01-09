import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
GRID_COLOR = (0, 0, 0)  # Black
BACKGROUND_COLOR = (200, 200, 200)  # Light Gray
CIRCLE_COLOR = (0, 0, 255)  # Blue
CROSS_COLOR = (255, 0, 0)  # Red
CIRCLE_RADIUS = 60
CROSS_WIDTH = 15
SPACE = 55

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND_COLOR)

# Game variables
board = [[None, None, None], [None, None, None], [None, None, None]]  # 3x3 grid
current_player = "X"  # Start with player X
game_over = False

# Draw the grid
def draw_grid():
    for i in range(1, 3):  # Draw two vertical and two horizontal lines
        # Vertical lines
        pygame.draw.line(screen, GRID_COLOR, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
        # Horizontal lines
        pygame.draw.line(screen, GRID_COLOR, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)

# Draw X
def draw_x(row, col):
    start_x = col * WIDTH // 3 + SPACE
    start_y = row * HEIGHT // 3 + SPACE
    end_x = (col + 1) * WIDTH // 3 - SPACE
    end_y = (row + 1) * HEIGHT // 3 - SPACE
    pygame.draw.line(screen, CROSS_COLOR, (start_x, start_y), (end_x, end_y), CROSS_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (start_x, end_y), (end_x, start_y), CROSS_WIDTH)

# Draw O
def draw_o(row, col):
    center_x = col * WIDTH // 3 + WIDTH // 6
    center_y = row * HEIGHT // 3 + HEIGHT // 6
    pygame.draw.circle(screen, CIRCLE_COLOR, (center_x, center_y), CIRCLE_RADIUS, CROSS_WIDTH)

# Check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Check for a draw
def check_draw():
    for row in board:
        if None in row:
            return False
    return True

# Main game loop
draw_grid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            clicked_row = mouse_y // (HEIGHT // 3)
            clicked_col = mouse_x // (WIDTH // 3)

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = current_player
                if current_player == "X":
                    draw_x(clicked_row, clicked_col)
                    current_player = "O"
                else:
                    draw_o(clicked_row, clicked_col)
                    current_player = "X"

                winner = check_winner()
                if winner:
                    print(f"{winner} wins!")
                    game_over = True

                elif check_draw():
                    print("It's a draw!")
                    game_over = True

    pygame.display.flip()

pygame.quit()
sys.exit()