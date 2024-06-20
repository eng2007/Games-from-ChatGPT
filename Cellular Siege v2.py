import pygame
import sys

class CellularSiege:
    def __init__(self, size=5, cell_size=80):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.players = {'A': 'X', 'B': 'O'}
        self.current_player = 'A'
        self.cell_size = cell_size
        self.window_size = (size * cell_size, size * cell_size)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Cellular Siege")

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for row in range(self.size):
            for col in range(self.size):
                pygame.draw.rect(self.screen, (0, 0, 0), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)
                font = pygame.font.Font(None, 36)
                text = font.render(self.board[row][col], True, (0, 0, 0))
                self.screen.blit(text, (col * self.cell_size + self.cell_size // 3, row * self.cell_size + self.cell_size // 3))

    def show_message(self, message):
        pygame.display.set_caption(f"Cellular Siege - {message}")
        pygame.time.delay(1500)  # Пауза для отображения сообщения

    def place_cell(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.players[self.current_player]
            self.capture_cells(row, col)
            self.switch_player()
        else:
            self.show_message("Эта ячейка уже занята. Попробуйте другую.")

    def capture_cells(self, row, col):
        player = self.players[self.current_player]
        self.capture_direction(row, col, 0, 1, player)  # Вправо
        self.capture_direction(row, col, 1, 0, player)  # Вниз
        self.capture_direction(row, col, 0, -1, player)  # Влево
        self.capture_direction(row, col, -1, 0, player)  # Вверх

    def capture_direction(self, row, col, dr, dc, player):
        row += dr
        col += dc
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = player

    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'A' else 'A'

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):
        pygame.init()
        while not self.is_board_full():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.cell_size
                    row = event.pos[1] // self.cell_size
                    self.place_cell(row, col)

            self.draw_board()
            pygame.display.flip()

        pygame.quit()
        self.show_winner()

    def show_winner(self):
        count_a = sum(row.count('X') for row in self.board)
        count_b = sum(row.count('O') for row in self.board)

        if count_a > count_b:
            print("Игрок A побеждает!")
        elif count_b > count_a:
            print("Игрок B побеждает!")
        else:
            print("Ничья!")


if __name__ == "__main__":
    game = CellularSiege(size=5, cell_size=80)
    game.play()
