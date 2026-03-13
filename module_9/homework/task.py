import tkinter as tk
from tkinter import messagebox
import random

class FifteenPuzzle:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Пятнашки")
        self.window.resizable(False, False)
        
        # Размер игрового поля: 4×4 клетки по 100 px
        self.cell_size = 100
        self.board_size = 4
        
        self.buttons = []
        self.empty_pos = (3, 3)  # Позиция пустой клетки (нижний правый угол)
        
        self.create_widgets()
        self.new_game()
    
    def create_widgets(self):
        """Создаёт игровое поле с кнопками."""
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                btn = tk.Button(
                    self.frame,
            text="",
            width=10,
            height=5,
            command=lambda x=i, y=j: self.move_tile(x, y)
                )
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)
        
        # Кнопка для новой игры
        tk.Button(self.window, text="Новая игра", command=self.new_game).pack(pady=10)
    
    
    def new_game(self):
        """Начинает новую игру: перемешивает плитки и размещает их на поле."""
        numbers = list(range(1, 16))  # Числа от 1 до 15
        random.shuffle(numbers)
        
        # Размещаем числа на поле
        for i in range(self.board_size):
            for j in range(self.board_size):
                if i == 3 and j == 3:  # Пустая клетка
                    self.buttons[i][j].config(text="", bg="lightgray")
                else:
                    self.buttons[i][j].config(
                    text=str(numbers.pop(0)),
                    bg="white"
                    )
        
        self.empty_pos = (3, 3)
        self.check_solvability()  # Проверяем, решаема ли расстановка
    
    
    def check_solvability(self):
        """Проверяет, решаема ли текущая расстановка плиток."""
        # Собираем все числа в один список (без пустой клетки)
        flat_board = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                text = self.buttons[i][j].cget("text")
                if text != "":
                    flat_board.append(int(text))
        
        # Считаем инверсии
        inversions = 0
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversions += 1
        
        # В 4×4 игре расстановка решаема, если:
        # - число инверсий чётно и пустая клетка в чётной строке (считая снизу)
        # - или число инверсий нечётно и пустая клетка в нечётной строке
        empty_row = self.empty_pos[0]
        from_bottom = self.board_size - empty_row  # Строка от нижнего края
        
        if (inversions % 2 == 0 and from_bottom % 2 == 1) or \
           (inversions % 2 == 1 and from_bottom % 2 == 0):
            return  # Решаема
        else:
            # Если не решаема — перемешиваем заново
            self.new_game()
    
    
    def move_tile(self, row, col):
        """Перемещает плитку, если это возможно."""
        # Проверяем, можно ли переместить плитку в пустую клетку
        if self.is_adjacent((row, col), self.empty_pos):
            # Меняем местами плитку и пустую клетку
            tile_text = self.buttons[row][col].cget("text")
            self.buttons[self.empty_pos[0]][self.empty_pos[1]].config(
            text=tile_text, bg="white"
        )
            self.buttons[row][col].config(text="", bg="lightgray")
            self.empty_pos = (row, col)
            
            # Проверяем победу
            if self.check_win():
                messagebox.showinfo("Победа!", "Вы собрали пятнашки!")
    
    
    def is_adjacent(self, pos1, pos2):
        """Проверяет, являются ли две позиции соседними."""
        row1, col1 = pos1
        row2, col2 = pos2
        return (abs(row1 - row2) == 1 and col1 == col2) or \
               (abs(col1 - col2) == 1 and row1 == row2)
    
    
    def check_win(self):
        """Проверяет, собрана ли игра."""
        expected = 1
        for i in range(self.board_size):
            for j in range(self.board_size):
                if i == 3 and j == 3:
                    continue  # Пропускаем пустую клетку
                text = self.buttons[i][j].cget("text")
                if int(text) != expected:
                    return False
                expected += 1
        return True
    
    
    def run(self):
        """Запускает главный цикл приложения."""
        self.window.mainloop()

# Запуск игры
if __name__ == "__main__":
    game = FifteenPuzzle()
    game.run()
