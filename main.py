import json

def save_games(games):
    with open('games.json', 'w', encoding='utf-8') as file:
        json.dump(games, file, ensure_ascii=False, indent=4)
            
def add_game(games):
    game = input('Какую игру ты хочешь добавить?')
    game = game.strip()
    if game == '':
        print('Пустое сообщение')
    else:
        games.append(game)
        save_games(games)
        
def show_games(games):
    if not games:
        print('Библиотека пуста')
    else:
        for number, game in enumerate(games, start=1):
            print(f'{number}. {game}')
            
def delete_game(games):
    if not games:
        print('Библиотека пуста')
    else:
        try:
            delete_number = int(input('Введи номер игры, которую хочешь удалить'))
        except ValueError:
            print('Введи число, а не слово')
            return
        
        if 1 <= delete_number <= len(games):
            game_to_delete = games[delete_number - 1]
            conf = input(f'Удалить игру {game_to_delete}?').strip().lower()
            if conf == 'да':    
                deleted_game = games.pop(delete_number - 1)
                print(f'Игра "{deleted_game}" удалена!')
                save_games(games)
            elif conf == 'нет':
                print('Удаление отменено')
                return
            else:
                print('Введи "Да" или "Нет"')
                return
        else:
            print('Такого номера нет в списке')
 
 
def load_games():
    try:
        with open('games.json', 'r', encoding='utf-8') as file:
            games = json.load(file)
            return games
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('Файл библиотеки поврежден')
        return []

   
games = load_games()

while True:
        
    print('==== PLAYLOG ====')
    print('1.Добавить игру \n 2.Показать библиотеку \n 3.Выйти \n 4. Удалить игру')
    print('Выбери действие')
    
    choice = input('Введи цифру действия которое тебе нужно')
    
    if choice == '1':
        add_game(games)
            
            
    elif choice == '2':
        show_games(games)
        
    elif choice == '3':
        break
    
    elif choice == '4':
        delete_game(games)
        
    else:
        print('Неверный выбор')