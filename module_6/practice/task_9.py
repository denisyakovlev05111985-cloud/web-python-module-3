"""
ЗАДАЧА: Анализ чатов пользователей

Даны сообщения в чате. Каждое сообщение представлено словарём
со следующими ключами:
- "user"      : имя пользователя (строка)
- "text"      : текст сообщения (строка)
- "timestamp" : время сообщения (целое число, возрастает не строго)

Пример входных данных:
messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Посчитать количество сообщений каждого пользователя.
   Результат сохранить в словарь вида:
   {
       "Алиса": 3,
       "Боб": 2
   }

2. Для каждого пользователя:
   2.1 Найти множество уникальных слов, которые он использовал
       (слова разделяются методом split()).
   2.2 Найти самое частое слово пользователя.
       Если самых частых слов несколько — можно выбрать любое.

3. Найти пользователя с самым большим словарным запасом,
   где словарный запас — это количество уникальных слов,
   использованных пользователем.

4. Найти множество слов, которые использовали ВСЕ пользователи
   (пересечение множеств слов пользователей).

5. Для каждого пользователя определить максимальный перерыв
   между его сообщениями:
   - перерыв = разница между timestamp текущего и предыдущего сообщения
   - найти пользователя с самым большим таким перерывом
"""

messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

messag_count= {}
user_words= {}


for message in messages:
    name= message["user"]
    text= message["text"]
    date= message["timestamp"]

    messag_count[name] = messag_count.get(name, 0) + 1

    user_words.setdefault(name, set()).update(text.split())
        
    
print(messag_count)
print(user_words)
        
max_frequent_word= {}

for el_name in user_words:
    frequent_word= {}
    for message in messages:
        if message["user"] == el_name:
            for word in message["text"].split():
                frequent_word[word] = frequent_word.get(word, 0) + 1
                
    max_word= None
    max_count= 0
    for word, count in frequent_word.items():
        if count > max_count:
            max_word= word
            max_count= count
    max_frequent_word[el_name] = max_word
print(max_frequent_word)

max_user_words= None
max_len= 0

for user, word in user_words.items():
    if len(user_words) > max_len:
        max_user_words = user
        max_len = len(word)
# if max_user_words != None:
print(max_user_words)

intersection_user_words= set.intersection(*user_words.values())
print(intersection_user_words)
# for name, texts in user_words.items():
#     if len(intersection_user_words) == 0:
#         intersection_user_words = texts
#         print(intersection_user_words)
# user_words = set.intersection()
    