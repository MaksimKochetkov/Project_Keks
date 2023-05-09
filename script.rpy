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
define mu = Character('Муха', color="#6b6875")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init:
    $morganie = ImageDissolve ("morganie.jpg", 1.0, 8)
    $morganieout = ImageDissolve ("morganie.jpg", 1.0, 8, reverse=True)
label start:

    stop music fadeout 1.0

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

    play music "music/Thank You For Your Patience.mp3"

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
    scene office with dissolve

    e "Страшно осознавать, что мне пришлось подниматься на 70 этаж"
    e "Хорошо, что тут непрозрачные лифты"
    sot "Там дальше наша любимая комната. Предлагаю угадать название"
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
    stop music fadeout 2
    pause 3
    play sound 'audio/lift_stop.ogg'
    stop sound
    scene minus_one
    play music "music/26 Black Lava.mp3"

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
    stop music
    pause 0.5
    play music "music/Thank You For Your Patience.mp3"


    e "Как я рада, что эта машина существует! Это буквально моя мечта! Ради этой работы я готова отдать всё! Буду самым лучшим работником на свете!"

    play sound 'audio/lift_stop.ogg'
    stop sound
    scene rabota

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
    show director at right with dissolve
    s "Здравствуйте, Анастасия."
    n "Здравствуйте.."
    s "Как закончите, заходите ко мне на 69 этаж. Проведём вступительный диалог."
    n "Я уже скоро буду"
    s "Замечательно. Жду."
    hide director
    e "Он мне очень знаком. Я точно его где-то видела!"
    sot "А почему вы не поехали с ним? Мы же закончили экскурсию?"
    n "Да как-то неловко просто"
    n "Я пойду как только закушу печеньку"
    sot "А вот это похвально!"
    stop music fadeout 0.5
    hide director with moveinright
    pause 3
    n "Теперь можно вызывать лифт"

    scene lift with dissolve:
        easeout 0.03 xalign .51
        easeout 0.03 yalign .49
        easeout 0.03 xalign .49
        easeout 0.03 yalign .51
        repeat
    play sound 'audio/lift.ogg' loop
    pause 1
    play sound 'audio/lift_stop.ogg'
    stop sound
    scene office with dissolve
    scene sigma_office with dissolve
    play music "music/Noriyuki_Iwadare_-_Godot_-_The_Fragrance_of_Dark_Coffee_Phoenix_Wright_Ace_Attorney_-_Trials_and_T_.mp3"

    s "Итак, я посмотрел ваше портфолио, вот что я могу сказать."
    s "Все эти милые вещи... тени, подбор цвета, композиция.."
    e "Мои работы должны быть для этой работы как раз кстати"
    e "Думаю, у меня идеальный стиль для этой машины"
    s "Ваша работа обгоняет по качеству только вентилятор."
    
    stop music
    show ventilator: 
        xalign 0 yalign 0.5
    play sound "audio/uououo.mp3"

    n "Но..."
    s "Но я всё равно вас беру. Но учтите, вы мне нужна только для квоты на 100 сотрудников,"
    s "Так что одно нарушение и вы уволены."
    n "Ясно... Ну хоть приняли..."
    n "Досвидания..."
    s "Ещё увидимся."

    hide director
    hide ventilator
    scene office with dissolve
    play music "music/isolation.mp3"

    "Мортис" "И она действительно пыталась впечатлить его ЭТИМ?"

    play sound 'audio/hahaha.mp3'

    "Эдгар" "Ахахахахахахахахаха"
    mu "Шатапнулись!"

    show muha xalign 0.4 with dissolve
    stop sound

    "Эдгар" "Эъ?"
    mu "От вас, как от рандомов в бравл старсе, толку ноль, а дизлайки ставить – так они первые. Не обращай на них внимания, я уверена, у тебя таланта больше, чем от этих двоих вместе взятых. Кстати, отличный галстук!"
    n "А… Спасибо большое. Прошу прощения, мне надо отойти…"
    e "Я все равно чувствую, как волнение накатывает на меня, поэтому бегу в туалет"

    

    play sound 'audio/topot.mp3'
    scene toilet with dissolve
    stop sound fadeout 1.0

    e "Надо успокоиться... Дыхательная гимнастика"
    e "Аааааааахх... Фууууууууух..."
    e "Аааааааахх... Фууууууууух..."
    e "Почему???"
    e "Почему всё так? Всё же было идеально?? Как так всё вышло?"
    e "Что мне теперь делать? Я специально переехала в город ради этой работы!!"
    e "Так, всё, спокойно, он меня взял, не надо расстраиваться. Фуф."
    e "Хааа... Не получается"
    e "Надо узнать как надо себя вести, чтобы не впасть ему в немилость"
    e "Пора идти в столовую, иначе я не успокоюсь"

    scene lift with dissolve:
        easeout 0.03 xalign .51
        easeout 0.03 yalign .49
        easeout 0.03 xalign .49
        easeout 0.03 yalign .51
        repeat
    play sound 'audio/lift.ogg' loop
    pause 1
    play sound 'audio/lift_stop.ogg'
    stop sound
    scene stolovaia with dissolve
    pause 2.0

    e "Ном"

    stop music fadeout 1.0

    e "Хорошо, что бургеры из мака тут тоже продают"
    e "Пора поиграть в Мику"

    image main_menu1 = Movie(play="movies/miku.webm")
    show main_menu1
    window hide dissolve
    pause 10
    show director at right

    s "Неплохо играешь."
    s "Лучше меня."

    scene stolovaia with dissolve
    show director at right

    n "Да?"
    e "Неожиданно за спиной босса появляется знакомый силуэт"
    mu "Здравствуйте, директор."

    play music "music/20 Blaster Cluster.mp3" loop

    s "Доброго дня, Муха. Вам что-то нужно?"
    mu "Нет-нет, я просто хотела поближе познакомиться с нашей новенькой. А ничто не объединяет лучше, чем еда из мака."
    s "Что ж, возможно, вы и правы. Я вообще считаю, что мак продает не еду, а общение… Тогда не буду отвлекать, наслаждайтесь симулякрами."

    hide director with dissolve
    pause 1

    mu "Можно присесть?"
    n "Да, конечно. Меня зовут Настя"
    mu "А я Муха, но ты уже поняла это. Рада знакомству"
    n "Взаимно. Можно один вопрос? Почему ты как-то занервничала в присутствии директора?"
    mu "С чего ты взяла?"
    n "Тебя выдали твой хвост, и вставшая шерсть на загривке. Ты показалась мне дружелюбной, но почему именно тебе не нравится директор"
    mu "А ты весьма наблюдательна. Знаешь, пока я не могу объяснить, даже самой себе. Но моя кошачья интуиция подсказывает, что что-то с ним не так… Но не будем об этом! Что тебе сказал директор по поводу твоего портфолио?"
    n "Что оно по уровню обгонит лишь вентилятор?"
    mu "А можно взглянуть?"
    e "Я протягиваю Мухе свое портфолио, она внимательно изучает его"
    mu "Ах он ребенок вошки! Да это же одно из самых лучших портфолио, которые я только видела в своей жизни. Я не ошиблась, когда сказала, что у тебя таланта больше, чем у тех двоих вместе взятых. Да у тебя его больше, чем у целой половины отдела"
    n "Ты правда так думаешь?"
    e "Кровь начала прилипать к щекам"
    mu "Разумеется!"
    n "Спасибо, мне очень приятно. Честно, я уже перестала верить в свои силы, но твоя похвала снова принесла мне вдохновение и мотивацию"
    mu "Хе-хе. Я очень рада. Мне кажется, твоих способностей хватило бы на целого кота"
    n "Погоди, что?"
    mu "Что?"
    n "Ты думаешь, мои работы действительно стоят того, чтобы засунуть их в ту самую машину по производству котов?"
    mu "Хм… Машину для производства котов уже давненько не запускали… Можно сказать, я одна из последних созданных кошек. Директор строго контролирует ее работу и никому не позволяет вставлять в нее рисунки."
    mu "Он говорит, что они недостаточно хороши, чтобы создать хотя бы одного разумного кота. Но твои работы. Мне кажется, они вполне способны снова запустить производство котов. Ты можешь спасти нашу расу от исчезновения!"
    n "Черт, я не думала, что обстановка так плоха… Тогда срочно нужно сходить с этой идеей к директору. И если он позволит мне создать кота, он сразу поймет, что я явно круче вентилятора!"
    n "И тогда все пойдет, как по маслу. Я поднимусь по карьерной лестнице, и эта работа станет больше, чем просто работой мечты. Муха, ты гений!"
    e "Я кидаюсь на шею к своей новой подруге"
    mu "Ха-ха-ха. Мне кажется, это явно отличная идея!"
    n "Тогда я побежала!"
    m "Удачи!"
    e "Я со всех ног забегаю в лифт и еду на 69 этаж"

    scene lift with dissolve:
        easeout 0.03 xalign .51
        easeout 0.03 yalign .49
        easeout 0.03 xalign .49
        easeout 0.03 yalign .51
        repeat
    play sound 'audio/lift.ogg' loop
    pause 1
    play sound 'audio/lift_stop.ogg'
    stop sound
    scene office with dissolve
    stop music fadeout 1.0

    e "Начинаю стучаться в кабинет директора"

    scene sigma_office with dissolve
    play music "music/Noriyuki_Iwadare_-_Godot_-_The_Fragrance_of_Dark_Coffee_Phoenix_Wright_Ace_Attorney_-_Trials_and_T_.mp3"

    s "Войдите. Что вы хотели?"
    n "Мне кажется, вы ошиблись, сравнив мое портфолио с вентилятором. Знаете ли, у меня был лучший учитель, ее звали Анастасией. И поэтому мои работы явно лучше, чем вы сказали. Я знаю про машину, которая питается милыми рисунками и создает котов, знаю, что ее очень давно не запускали."
    n "Так прошу, дайте мне шанс! Если у меня все получится, вы сразу поймете, что я представляю собой большее, чем вы думаете!"
    s "Исключено."
    n "Что?.."
    s "Это исключено. Я понимаю, вы полны энтузиазма, вас взяли в такую шикарную компанию, несмотря на несколько посредственные работы. Можете злиться на меня, я директор, представляющий интересы этой компании уже много лет, поэтому я не могу вам льстить."
    s "К тому же вы не думали, что что-то может пойти не так? Я не зря столько лет не позволял никому запускать эту машину. Все эскизы недостаточно хороши, и если вставить их в котодельную машину, может произойти непоправимое."
    s "Случится КОТОстрофа. Можно создать неразумных котов, мутантов, и тому подобное. К тому же, машина может выпустить их в огромном количестве, они могут вырваться в город и кому-то навредить. Тогда их придется истреблять, а это может сказаться и на обычных гражданах."
    s "К тому же, так можно по неосторожности убить разумного кота, а их итак осталось мало. Создание жизни – огромная ответственность. Неужели вы не подумали о рисках?"
    n "Наверно, нет"
    s "Тогда уходите, и не занимайтесь ерундой, а попробуйте хоть немного поработать. А не то вас в скором времени придется уволить, и вы лишитесь того, к чему так долго шли."
    n "Да, директор. Простите, что потратила ваше время"

    window hide dissolve
    pause 1

    s "Черт, это Муха ее натолкнула. Кажется, нужно будет внимательнее смотреть за обеими…"

    scene office with dissolve

    n "Не могу поверить, что он не готов даже дать мне шанса. А что, если он прав… Мне не стоит даже пытаться. Но… Учительница же всегда хвалила мои рисунки котов. Это то, что у меня действительно хорошо получается. Она была профессионалом своего дела и не могла ошибиться на мой счет."
    n "Что, если попытаться сделать кота самой. Никакой КОТОстрофы не случится. Возможно, я создам кого-то по типу Мухи. Она же настоящая крутышка. Мои рисуки не могут быть так плохи."
    n "А если все пройдет удачно, ему уж точно ничего не останется, кроме как признать мои способности! Дождусь вечера, и спущусь на самый нижний этаж «1000-7» к котодельной машине."

    stop music fadeout 2.0

    e "За работой незаметно, как проходит день"

    scene rab
    pause 3
    scene office
    pause 1

    e "Многие сотрудники уже почти разошлись. Думаю, пора, пока здание не закрыли"

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
    scene minus_one with dissolve

    e "Вот она…"

    play sound "audio/mashina.mp3" loop volume 0.25 fadein 3.0

    e "Я аккуратно жму кнопки, тяну рычаг. Машина медленно запускается. Когда она готова к работе, вставляю свой рисунок"
    n "Так, а теперь немного подождем"
    e "Процесс почти завершился"
    e "Неожиданно из машины выпрыгивает огромная серая кошка. Выпучив глаза, она бросается к лестнице наверх"

    play audio "audio/zlaya_mishel.mp3"

    n "Стой, подожди!"

    play audio "audio/topot.mp3"
    stop sound fadeout 5

    e "Бегу за ней, но никак не могу догнать. Адреналин не дает мне устать даже от такого подъема"

    scene rabota with dissolve

    e "Однако все зря. Кошка выбегает в коридор, где ее видят испуганные сотрудники и меня, выбегающую следом." 

    play audio "audio/steklo.mp3"

    e "Проносясь мимо ошарашенных людей, кошка выпрыгивает в открытое окно и исчезает в темном свете улицы"
    e "На меня смотрят сотрудники, только сейчас я понимаю, как сильно устала и начинаю пытаться отдышаться."

    show muha with dissolve

    e "Замечаю на себе удивленный взгляд Мухи,"
    e "Вижу язвительные ухмылки Мортиса и Эдгара."
    e "За спиной слышу знакомый голос."

    show director at right with dissolve
    pause 1

    s "Что это все значит?"

    hide muha with dissolve

    n "Ой.. А я.. Это.."
    e "От злости у него терлись зубы"
    e "Ещё бы чуть-чуть, и начала бы виднеться вена на лбу"
    s "*Вздох*"
    s "Иди домой. Ты переводишься на дистанционную работу на неделю."
    s "Потом как найдём ещё одного сотрудника, сразу вышвырнем тебя за шкирку."
    n "..."
    e "На меня смотрели абсолютно все собравшиеся на первом этаже, кроме, как оказалось Мухи"
    e "Её тут не было. Она меня бросила?"
    s "Направляйся домой. Прямо сейчас."
    n "Хорошо..."

    scene street with dissolve 
    pause 2
    play music "music/isolation.mp3"

    e "Он взял меня с неохотой."
    e "Я должна была вести себя примерно, но сделала всё только хуже"
    e "Вот так вот мечта может рухнуть в один момент. И с этим ничего не сделаешь. Как это угнетает."

    pause 2
    scene bg room with dissolve

    d "Привет, Настя!! Как дела???"
    n "Всё плохо, Дима"
    d "А почему??"

    pause 4
    scene bg room with fade

    e "Я рассказала ему о сегодняшнем дне. Вряд-ли он что-то предложит сделать, но я не могу это не рассказать"
    d "А почему тогда он вообще держит этот бизнес, если машина не работает?"
    n "А ведь точно... Как он получает прибыль?"
    d "Попробуй узнать"

    scene office with fade
    mu ""



    return
