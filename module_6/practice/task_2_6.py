import random

def generate_number():
    
    return random.randint(1000, 9999)

def check_guess(secret_number, user_guess):
    
    bulls = 0
    cows = 0
    
    str_secret = str(secret_number)
    str_guess = str(user_guess)
    
    for i in range(4):
        if str_secret[i] == str_guess[i]:
            bulls += 1
        elif str_secret[i] in str_guess:
            cows += 1
    
    return bulls, cows

def play_game():
    global attempts
    attempts += 1 
    
    secret_number = generate_number()
    print(f"Загаданное число: {secret_number}")
    
    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            if user_guess < 1000 or user_guess > 9999:
                print("Число должно быть четырёхзначным!")
                continue
            
            bulls, cows = check_guess(secret_number, user_guess)
            
            if bulls == 4:
                print(f"\nПоздравляем! Вы угадали число за {attempts} попыток!")
                break
            else:
                print(f"Быков: {bulls}, Коров: {cows}")
                
        except ValueError:
            print("Пожалуйста, введите корректное число!")

attempts = 0

print("Добро пожаловать в игру 'Быки и коровы'!")
play_game()
