from django.shortcuts import render, redirect

WRITERS_DATA = {
    'Hemingway': {
        'name': 'Эрнест Хемингуэй',
        'bio': 'Американский писатель, лауреат Нобелевской премии.',
        # Добавим года для книг, чтобы можно было фильтровать
        'books': [
            {'title': 'Старик и море', 'year': 1952},
            {'title': 'По ком звонит колокол', 'year': 1940},
            {'title': 'И восходит солнце', 'year': 1926},
        ]
    },
    'Shakespeare': {
        'name': 'Уильям Шекспир',
        'bio': 'Английский поэт и драматург.',
        'books': [
            {'title': 'Гамлет', 'year': 1600},
            {'title': 'Ромео и Джульетта', 'year': 1595},
        ]
    }
}

BOOKS_TOP = [
    {'title': 'Война и мир', 'author': 'Л. Н. Толстой', 'year': 1869, 'desc': 'Эпический роман о судьбах людей на фоне войны 1812 года.'},
    {'title': 'Преступление и наказание', 'author': 'Ф. М. Достоевский', 'year': 1866, 'desc': 'Психологический роман о преступлении и искуплении.'},
    {'title': 'Анна Каренина', 'author': 'Л. Н. Толстой', 'year': 1877, 'desc': 'Трагическая история любви в контексте общества XIX века.'},
    {'title': 'Отцы и дети', 'author': 'И. С. Тургенев', 'year': 1862, 'desc': 'Роман о конфликте поколений и идей.'},
    {'title': 'Герой нашего времени', 'author': 'М. Ю. Лермонтов', 'year': 1840, 'desc': 'Первый в русской литературе психологический роман.'},
    {'title': 'Старик и море', 'author': 'Эрнест Хемингуэй', 'year': 1952, 'desc': 'Повесть о старом рыбаке, который борется с гигантским марлином в открытом море.'}
]

def home(request):
    return render(request, 'home.html', {'title': 'Главная'})

def writers_list(request):
    return render(request, 'writers.html', {
        'title': 'Писатели',
        'writers': WRITERS_DATA.keys()
    })

def writer_detail(request, name):
    if name in WRITERS_DATA:
        return render(request, 'writer_detail.html', {
            'title': WRITERS_DATA[name]['name'],
            'writer': WRITERS_DATA[name]
        })
    else:
        return redirect('writers')

# Новая функция для задания 5: фильтрация по автору и году
def writers_filtered(request):
    writer_name = request.GET.get('writers')  # параметр writers из URL
    year_str = request.GET.get('year')        # параметр year из URL

    # Если параметров нет — можно просто показать список писателей
    if not writer_name:
        return redirect('writers')

    # Ищем писателя по ключу (Hemingway, Shakespeare и т.д.)
    if writer_name not in WRITERS_DATA:
        return redirect('writers')

    writer = WRITERS_DATA[writer_name]

    # Если год не передан — показываем все книги писателя
    if not year_str:
        filtered_books = writer['books']
        has_results = len(filtered_books) > 0
    else:
        # Пытаемся преобразовать год в число
        try:
            year = int(year_str)
        except ValueError:
            # Если год некорректный — редирект на писателя
            return redirect('writer_detail', name=writer_name)

        # Фильтруем книги по году
        filtered_books = [b for b in writer['books'] if b['year'] == year]
        has_results = len(filtered_books) > 0

    context = {
        'title': f'Книги {writer["name"]} ({year_str or "все годы"})',
        'writer_name': writer['name'],
        'filtered_books': filtered_books,
        'year_filter': year_str,
        'has_results': has_results,
    }

    # По условию: если информации за указанный год нет — редирект на страницу писателя
    if year_str and not has_results:
        return redirect('writer_detail', name=writer_name)

    return render(request, 'writers_filtered.html', context)

def books(request):
    context = {'title': 'Топ лучших книг', 'books': BOOKS_TOP}
    return render(request, 'books.html', context)

def book_detail(request, position):
    if 1 <= position <= len(BOOKS_TOP):
        book = BOOKS_TOP[position - 1]
        return render(request, 'book_detail.html', {
            'title': f'Книга #{position}: {book["title"]}',
            'book': book,
            'position': position
        })
    return redirect('books')

def book_by_slug(request, book_slug):
    slug_to_title = {'the_Sea': 'Старик и море'}
    title = slug_to_title.get(book_slug)
    if not title:
        for b in BOOKS_TOP:
            if book_slug.lower() in b['title'].lower():
                title = b['title']
                break

    if title:
        for book in BOOKS_TOP:
            if book['title'] == title:
                return render(request, 'book_detail.html', {
                    'title': book['title'],
                    'book': book,
                })
    return redirect('writer_detail', name='Hemingway')
