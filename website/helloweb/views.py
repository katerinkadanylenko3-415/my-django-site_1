# from django.shortcuts import render
# from django.http import HttpResponse
# import datetime
# from django.views import View
#
# import random
# from django.http import HttpResponse






# def index(request):
#     return HttpResponse("""
#            <h1>Hello from my first views function !</h1>
#     """)
#
# data = [1, 2, 3, 4, 5]

# def current_datetime(request):
#     now = datetime.datetime.now()
#     return HttpResponse(f"""
#            <h1>Current datetime : {now} </h1>
#            <p>data: {data} </p>
#     """)

# class CurrentDataTime(View):
#
#     def get(self, request):
#         now = datetime.datetime.now()
#         return HttpResponse(f"""
#
#           <h1>Current datetime: {now}</h1>
#           <p>Data {data}</p>
# """)
#
# quotes_list = [
#         "Код працює? Не чіпай! (Народна мудрість)",
#         "Програмування — це на 10% написання коду і на 90% роздуми, чому він не працює.",
#         "Hello World — це початок великого шляху.",
#         "Помилки — це просто досвід, оформлений у консолі."
#     ]
#
# def get(request):
#     quote_list = random.choice(quotes_list)
#     return HttpResponse(f"""
#           <h1>Випадкова цитата:</h1>
#           <p>{quote_list}</p>
# """)

from django.http import HttpResponse


#1
def index(request):
    return HttpResponse("""
        <h1>Головна сторінка</h1>
        <p>Ласкаво просимо на портал міста Києва!</p>
        <a href="/news/">Новини</a><br>
        <a href="/management/">Голови міста</a><br>
        <a href="/facts/">Факти</a><br>
        <a href="/contacts/">Контакти</a><br>
        <a href="/history/">Історія</a>
    """)


def news(request):
    return HttpResponse("""
        <h1>Новини міста</h1>
        <p>У Києві відкрили новий парк.</p>
        <a href="/">На головну</a>
    """)


def management(request):
    return HttpResponse("""
        <h1>Голови міста</h1>
        <p>Чинний мер: Віталій Кличко</p>
        <a href="/">На головну</a>
    """)


def facts(request):
    return HttpResponse("""
        <h1>Факти про місто</h1>
        <ul>
            <li>Заснований у V столітті</li>
            <li>Стоїть на Дніпрі</li>
            <li>Столиця України</li>
        </ul>
        <a href="/">На головну</a>
    """)


def contacts(request):
    return HttpResponse("""
        <h1>Контактні телефони</h1>
        <p>Поліція — 102</p>
        <p>Швидка — 103</p>
        <p>Пожежна — 101</p>
        <a href="/">На головну</a>
    """)

def history(request):
    return HttpResponse("""
        <h1>Історія міста</h1>
        <p>Київ — одне з найстаріших міст Європи.</p>
        <a href="/history/people/">Відомі мешканці</a><br>
        <a href="/history/photos/">Історичні фото</a><br>
        <a href="/">На головну</a>
    """)


def history_people(request):
    return HttpResponse("""
        <h1>Відомі мешканці</h1>
        <p>Тарас Шевченко</p>
        <p>Михайло Грушевський</p>
        <a href="/history/">Назад</a>
    """)


def history_photos(request):
    return HttpResponse("""
        <h1>Історичні фотографії</h1>
        <p>Тут можуть бути старі фото Києва.</p>
        <a href="/history/">Назад</a>
    """)

from django.http import HttpResponse


def base_page(title, content):
    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>

        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">

        <style>
            body {{
                margin: 0;
                background: linear-gradient(#9932CC, #9370DB, #FF00FF);
                color: white;
                text-align: center;
            }}

            nav {{
                background: rgba(0,0,0,0.4);
                padding: 15px;
            }}

            nav a {{
                color: white;
                text-decoration: none;
                margin: 15px;
                font-weight: 600;
                transition: 0.3s;
            }}

            nav a:hover {{
                color: #ffd700;
            }}

            .container {{
                padding: 40px;
            }}

            img {{
                width: 60%;
                border-radius: 10px;
                margin-top: 20px;
            }}

            .card {{
                background: rgba(255,255,255,0.1);
                padding: 20px;
                margin: 20px auto;
                width: 60%;
                border-radius: 10px;
            }}

            h1 {{
                color: #ffd700;
            }}
        </style>
    </head>
    <body>

    <nav>
        <a href="/">Головна</a>
        <a href="/news/">Новини</a>
        <a href="/management/">Голови</a>
        <a href="/facts/">Факти</a>
        <a href="/contacts/">Контакти</a>
        <a href="/history/">Історія</a>
    </nav>

    <div class="container">
        {content}
    </div>

    </body>
    </html>
    """

def index(request):
    content = """
        <h1>Ласкаво просимо до Києва</h1>
        <p>Столиця України, місто історії та сучасності.</p>
        <img src="https://visitukraine.today/media/blog/previews/4F7cVmsKNRZ6tw3yTtrE5IZQF10C6qnyePAwuJUl.webp">
    """
    return HttpResponse(base_page("Головна", content))


def news(request):
    content = """
        <h1>Новини міста</h1>

        <div class="card">
            <h3>Відкриття нового парку</h3>
            <p>У центрі міста з'явилась нова зелена зона.</p>
        </div>

        <img src="https://cdn.village.com.ua/the-village.com.ua/post_image-image/DBMCAg1Eb2x0bwITC2sR9g-original_opt.webp">
        <img src="https://kyiv.comments.ua/img/publications/880x586/QZSk4F4j5lFaA1tCPqxe58hiLjSnL0wm.jpg">
        <img src="https://kyiv24.news/wp-content/uploads/2025/07/2photo_2025-07-22_14-04-19-1024x768.jpg">
        <img src="https://cdn.informator.ua/@prod/media/kiev/2025/10/14/68ee60b0d84cb4.70672452.png">
        <img src="https://i.ytimg.com/vi/oPIFL92D-g0/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDsbmIjJxgbMBmHA9GtkRkmUd1X0Q">
    """
    return HttpResponse(base_page("Новини", content))


def management(request):
    content = """
        <h1>Голова міста</h1>
        <p>Чинний мер — Віталій Кличко</p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/2014-09-12_-_Vitali_Klitschko_-_9019.jpg">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/VladimirVitaliy.jpg/250px-VladimirVitaliy.jpg">
    """
    return HttpResponse(base_page("Голови", content))


def facts(request):
    content = """
        <h1>Цікаві факти</h1>

        <div class="card">
            <p>• В XI столітті Київ був справжнім мегаполісом — він був у 50 разів більшим за Лондон і в 10 разів більшим за Париж.</p>
            <p>• Станція метро «Арсенальна» довгий час вважалася найглибшою у світі (105,5 метрів). Поїздка на її ескалаторах триває близько 5 хвилин.</p>
            <p>• Головна вулиця, Хрещатик, є однією з найкоротших центральних вулиць світу (лише 1,2 км), але водночас однією з найширших (до 100 м). Найдовша ж вулиця міста — Броварський проспект довжиною 14 км.</p>
            <p>• Київ відомий як «каштанова столиця». Окрім каштанів, тут розташований один із найбільших міських парків Європи — Голосіївський.</p>
            <p>• Знаменитий «Київський торт» з’явився у 1956 році через помилку кондитерів, які забули поставити білки в холодильник, а «Київська перепічка» на Театральній стала гастрономічною легендою, що не змінює рецепт уже десятиліттями.</p>
            <p>• Найвідоміше «місце сили». За переказами, саме тут збираються відьми на свої шабаші. На горі досі збереглося язичницьке капище з ідолом Перуна, що дивиться на всі чотири сторони.</p>
            <p>• Архітектор Городецький прикрасив свій дім бетоними головами слонів, носорогів та морських чудовиськ. Легенда каже, що він зробив це в пам'ять про доньку, яка нібито втопилася (насправді вона прожила довге життя), а сам будинок начебто прокляв перед від'їздом.</p>
            <p>• Андріївська церква: З її тераси відкривається один із найкращих видів на Поділ, Дніпро та район Воздвиженка.</p>
            <p>• У підвальному приміщенні на вул. Володимирській, 43, розташована церква Марії Магдалини. Це найменший діючий храм міста.</p>
            <p>• Офіційною датою заснування міста вважається 482 рік. У 2025 році Києву виповнюється 1543 роки.</p>
        </div>
    """
    return HttpResponse(base_page("Факти", content))


def contacts(request):
    content = """
        <h1>Контакти служб</h1>

        <div class="card">
            <p>Поліція — 102</p>
            <p>Швидка — 103</p>
            <p>Пожежна — 101</p>
        </div>
    """
    return HttpResponse(base_page("Контакти", content))

def history(request):
    content = """
        <h1>Історія міста</h1>
        <p>Київ заснований у V столітті.</p>

        <a href="/history/people/">Відомі мешканці</a><br><br>
        <a href="/history/photos/">Історичні фото</a>
    """
    return HttpResponse(base_page("Історія", content))

def history_people(request):
    content = """
        <h1>Відомі мешканці</h1>
        <p>Тарас Шевченко</p>
        <p>Михайло Грушевський</p>
        <p>Ігор Сікорський</p>
        <p>Борис Патон</p>
        <p>Михайло Булгаков</p>
        <p>Олександр Архипенко</p>
        <p>Іван Барський</p>
        <p>Голда Меїр</p>
        <p>Валерій Лобановський</p>
        <p>Леся Українка</p>
        <p>Катерина Осадча</p>
        <p>Євгенія Мірошниченко</p>
    """
    return HttpResponse(base_page("Відомі мешканці", content))

def history_photos(request):
    content = """
        <h1>Галерея Києва</h1>

        <div class="gallery">
            <img src="https://info-ua.net/wp-content/uploads/2024/09/istoria-rozvitku-1.jpg">
            <img src="https://tykyiv.com/media/11.JPG">
            <img src="https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/fac8/live/13b1cd90-4047-11ef-8af1-7d28c9a79969.jpg.webp">
            <img src="https://24tv.ua/resources/photos/news/202105/1640208_15048343.jpg?202105114952&w=2200&h=1522&fit=cover%27&output=webp">
            <img src="https://kor.ill.in.ua/m/1260x900/1453980.jpg">
            <img src="https://i.obozrevatel.com/gallery/2023/10/9/383995802733033125530331552999776121414413n.jpg">
            <img src="https://etoretro.ru/data/media/24/1526455972cd3.jpg">
            <img src="https://babel.ua/static/content/nf3ydfsy/thumbs/660x371/4/ee/0898bae5662b8c4a9cd8ea2db1fa7ee4.jpg?v=2705">
        </div>
    """
    return HttpResponse(base_page("Фото", content))

from django.shortcuts import render
import datetime

# def index(request):
#     list1 = ['1', '2', '3']
#     context = {'title': "First data context in render",
#                'text': "add some text in P tes",
#                'today': datetime.date.now(),
#                'datalist': list1}
#     return render(request, 'blog/index.html', context)
