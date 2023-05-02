﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

define e = Character(' ', color="#c8ffc8")
#мысли гг
define n = Character('Настя', color="#00b7ff")
define d = Character('Дима', color="#b5ce47")
define f = Character('Фрося', color="#5e5e5e")
define k = Character('Кекс', color="#111111")
define m = Character('Мишель', color="#494949")
define s = Character('Директор', color="#9558ff")
#siiigma
define ko = Character('Коллега', color="#686868")
define sot = Character('Сотрудница', color="#be98ff")
define sotm = Character('Сотрудница', color="#49336e")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init:
    $morganie = ImageDissolve ("morganie.jpg", 1.0, 8)
    $morganieout = ImageDissolve ("morganie.jpg", 1.0, 8, reverse=True)
label start:

    centered "{bt=3}{color=#FFF}С момента окончания колледжа прошло много лет.{/color}{/bt}"

    play music 'music/isolation.mp3'

    centered "{bt=3}{color=#FFF}Я давно не видела не только одногрупников, но и родителей.{/color}{/bt}"
    centered "{bt=3}{color=#FFF}Конечно, я ведь живу в другом городе.{/color}{/bt}"
    centered "{bt=3}{color=#FFF}Теперь я устроилась на кое-какую работу.{/color}{/bt}"
    centered "{bt=3}{color=#FFF}Этот день мог не слишком сильно отличиться от любых других.{/color}{/bt}"
    centered "{bt=3}{color=#FFF}Да, я вливаюсь в новый коллектив.{/color}{/bt}"
    centered "{bt=3}{color=#FFF}Но это всё равно не сравнится с прошлыми, в том числе с колледжевскими друзьями.{/color}{/bt}"
    centered "{bt=3}{color=#FFF}Даже не смотря на это, именно сегодня начинается эта причудливая история.{/color}{/bt}"
    centered "{w=2}{nw}"

    stop music fadeout 2
    $renpy.movie_cutscene("movies/6am.webm")
    play music 'music/alarm.ogg'
    scene closed

    # show eileen happy

    e "..."
    e "Ох, уже утро…"

    play sound shelk
    stop music
    scene bg room with morganie

    e "Точно! Это же будет мой первый день на работе. Работе моей мечты"

    play music 'music/daylight.mp3'

    e "Нужно как можно скорее собраться, чтоб не опоздать"
    e "Так. Где же мой розовый галстук?"

    pause 5

    e "Я готова, пора выдвигаться"

    play music 'music/dima.mp3'

    d "Стоой. Ты никогда не угадаешь, что у меня есть!"
    n "Я могу опоздать на работу, мне некогда играть в угадайку"
    d "Раз работа тебе кажется более впечатляющей, чем это, то мне тебя жаль..."
    e "Дима протянул мне какую-то игрушку"

    scene sirenogolovii with dissolve

    n "ЧТО. Это фигурка сиреноголового??? "
    d "Даа!!!"
    n "Жеесть, я завидую."

    scene bg room with dissolve

    e "Я посмотрела на часы"

    play music 'music/firstleap.mp3'
    play sound 'audio/topot.mp3' loop

    n "О НЕТ. Время несется как ультующий Булл. Я же опоздаю."

    scene street with dissolve

    n "Пришлось в спешке выбежать из дома, ужас!"
    n "Как же так.."

    e "/На светофоре загорается красный/"

    stop sound

    n "Черт. Почему именно сейчас?!"
    e "Как только загорается зеленый, я сразу начинаю бежать изо всех сил"

    play sound 'audio/topot.mp3' loop

    n "ООЙ"

    stop sound
    scene street with hpunch
    play sound "audio/punch.opus"
    stop music fadeout 1
    show frosya

    f "Куда вы так торопитесь?"
    n "Простите, я не хотела! Просто я очень опаздываю на работу. Сегодня мой первый рабочий день, и я очень хочу произвести хорошее впечатление."
    f "Вот как. А где вы работаете, может я подскажу короткий путь?"
    n "“Поук энд Пирс” на Вулф-Стрит."
    f "Хихихиха, вы выбрали не самый короткий путь. Не так давно переехали в этот город?"
    n "Все так"
    f "После следующего светофора поверните налево, на улицу Кукирана. После через переход на Кэт-Стрит, а оттуда сразу выйдете к “Поук энд Пирс ”."

    play sound 'audio/topot.mp3' loop

    n "Спасибо вам огромное!"
    f "Кажется, добром это не кончится. Сожрут ее бедную…"

    scene rabota with dissolve
    stop sound

    n "Фух, вовремя..."
    n "Здравствуйте, я пришла на первый день на работу"
    e "За стойкой сидела женщина. Она с неохотой подняла голову"
    sot "Здравствуйте."
    sot "Прежде, чем мы начнём, я проведу вам экскурсию."
    n "Поняла"
    sot "Пройдёмте за мной."
    e "Вместе мы пришли к лифту"

    scene lift with dissolve:
        easeout 0.03 xalign .51
        easeout 0.03 yalign .49
        easeout 0.03 xalign .49
        easeout 0.03 yalign .51
        repeat
    play sound 'audio/lift.ogg' loop

    n "А мы долго будем ехать?"
    sot "Нет, всего лишь десятки этажей выше"

    pause 3
    play sound 'audio/lift_stop.ogg'
    stop sound
    scene office

    e "Страшно осознавать, что мне пришлось подниматься на 70 этаж"
    e "Хорошо, что тут непрозрачные лифты"
    sot "Это наша любимая комната. Предлагаю угадать название"
    n "Как я должна угадать? Я же тут впервые!"
    sot "Да не бойтесь, угадает даже тот, кто не видел нас в лицо."
    n "Нуу... Столовая.."
    e "Предположила я в шутку"
    sot "Как же вы правы! Хорошо тут приживётесь!"
    n "Но ведь столовые всегда располагаются на первом этаже? Чтобы было легче доставлять еду"
    sot "Да ничего, нам всё доставляют на вертолётах"
    n "Ну ничего себе..."
    sot "А теперь вниз."
    "Мортис" "Погодите!"
    e "Передо мной резко приземляется Эдгар на ульте"
    "Эдгар" "Мы увидели новичка в нашей компании... Не частое явление!"
    "Эдгар" "В честь утешительного приза я хочу подарить тебе.. Шоколадку.. {cps=*2}АХАХАХХАХАХХАХАХАХАХААХАХХА{/cps}"
    "Мортис" "Балда! Всё испортил своим смехом. Из-за слова теперь смеяться будешь? Это же всего лишь шокола... {cps=*2}АХАХАХАХХАХАХАХАХАХХАХАХААХАХА{/cps}"
    e "Потом они просто скрылись, не успела я и моргнуть глазом"
    e "А шоколадку мне так и не отдали"
    sot "Не обращай на них внимания. Помните старый сериал Кухня? Там ещё были повара Сеня и Федя? Вот тут то же самое."
    sot "Но это не важно. Теперь время для самого главного."

    scene lift with dissolve:
        easeout 0.03 xalign .51
        easeout 0.03 yalign .49
        easeout 0.03 xalign .49
        easeout 0.03 yalign .51
        repeat
    play sound 'audio/lift.ogg' loop
    pause 3
    play sound 'audio/lift_stop.ogg'
    stop sound
    scene minus_one

    e "-1 этаж был пустоват. Лишь в конце комнаты одна из стен была металлической"
    e "Но это не стена. Это специальная машина по созданию человекоподобных кошек"
    e "Она настолько же огромная, насколько большими были компьютеры в 70-е годы. Своими размерами занимает всю стену"
    e "В ней виднелось отверстие для бумаги, а левее располагался дверной проём, откуда, скорее всего, выходили коты"
    sot "Это главная звезда нашего предприятия. Без неё нас бы тут не было и я работала уборщицей."
    n "Хаха, что-что?"
    sot "Не обессудьте, это у меня такой юмор."
    sot "Думаю, вы знаете, что делает эта машина. У меня лишь один вопрос. Есть ли у вас вопросы по её работе?"
    n "Что будет, если дать машине рисунок, содержащий негативные образы?"
    sot "Мы не проверяли такого. Но будет что-то явно нехорошее."
    sot "Ещё вопросы?"
    n "Ну, думаю, теперь я уже всё знаю"
    sot "Отлично, тогда короткая техника безопасности:"
    sot "1. Руки никуда не совать."
    sot "2. За дверь проход разрешён только инженерам уровня 3."
    sot "3. Бумага не должна быть жирной или содержать любую другую грязь."
    sot "На этом всё."
    sot "Так как директор ещё не приехал, пройдём вглубь первого этажа, в комнату отдыха."
    sot "Почему-то он захотел лично заняться вами."

    scene lift with dissolve:
        easeout 0.03 xalign .51
        easeout 0.03 yalign .49
        easeout 0.03 xalign .49
        easeout 0.03 yalign .51
        repeat
    play sound 'audio/lift.ogg' loop
    pause 0.5

    e "Как я рада, что эта машина существует! Это буквально моя мечта! Ради этой работы я готова отдать всё! Буду самым лучшим работником на свете!"

    play sound 'audio/lift_stop.ogg'
    stop sound
    scene office

    sot "Поворачивайте налево и идёте до конца, там уже найдёте чай и прочие..."
    sotm "Маша, тихо! Босс идёт, нельзя разговаривать!"
    play music "music/darkage.mp3"
    sot "Что? Когда он успел прийти?"
    image main_menu = Movie(play="movies/director.webm")
    show main_menu
    window hide dissolve
    pause 12
    window show dissolve
    hide main_menu
    show director at right
    s "Здравствуйте, Анастасия."
    n "Здравствуйте.."
    s "Как закончите, заходите ко мне на 69 этаж. Проведём вступительный диалог."
    n "Я уже скоро буду"
    s "Замечательно. Жду."
    e "Он мне очень знаком. Я точно его где-то видела!"
    sot "А почему вы не поехали с ним? Мы же закончили экскурсию?"
    n "Да как-то неловко просто"
    n "Я пойду как только закушу печеньку"
    sot "А вот это похвально!"
    hide director with moveinright
    return
