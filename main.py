import telebot # 4.9.0 version library
from telebot import types

bot = telebot.TeleBot('5774241921:AAGgH8INawmd9HN0nZ8imnHwthKKOJ0dq_4', parse_mode='html')

the_user = []
with open('data/user.txt') as f:
    for line in f:
        the_user.extend([int(x) for x in line.split()])

the_key = []
with open('data/key.txt') as f:
    for line in f:
        the_key.extend([str(x) for x in line.split()])


def up_data(a_user, a_key):
    with open('user.txt', 'wb'):
        pass
    with open('key.txt', 'wb'):
        pass

    f1 = open('user.txt', 'w')
    f2 = open('key.txt', 'w')

    user_612 = list(map(str, a_user))
    key_612 = list(map(str, a_key))

    user_f = str(' '.join(user_612))
    key_f = str(' '.join(key_612))

    f1.write(user_f)
    f2.write(key_f)


@bot.message_handler(commands=['start'])
def welcome(m):
    cid = m.chat.id  # get user info
    if cid in the_user:
        pass

    else:
        bot.send_message(cid, 'Ви не маєте доступу до бота\nДе купити доступ - @glebmandziy')
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Схема по скаму 1")
    item2 = types.KeyboardButton("Схема по скаму 2")
    item3 = types.KeyboardButton("Схема по скаму 3")
    item4 = types.KeyboardButton("Схема по скаму 4")
    item5 = types.KeyboardButton("Схема по скаму 5")
    item6 = types.KeyboardButton("Схема по скаму 6")
    item7 = types.KeyboardButton("Схема по скаму 7")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(cid,
                     "Привіт, <b>{0.first_name}</b>!\nЯ допоможу тобі заскамити русню, вибери в меню схему скаму".format(
                         m.from_user, bot.get_me()),reply_markup=markup)


@bot.message_handler(commands=['what_user'])
def welcome(message):
    bot.send_message(message.chat.id, f'User: {len(the_user)}\nНо не забывай что это считаются и аккаунты админов😎😎😎')


@bot.message_handler(content_types=['text'])
def main(m):
    cid = m.chat.id  # get user info
    key = m.text
    if m.chat.type == 'private':
        if key in the_key:
            the_user.append(m.chat.id)
            bot.send_message(m.chat.id,
                             'Ви оформили підписку!\nДякую за покупку☺️. Перезапустіть бота командою /start для користування')
            the_key.remove(key)
            up_data(the_user, the_key)

        elif cid in the_user:
            if m.text == 'Схема по скаму 1':
                bot.send_message(m.chat.id,
                            "<b>Схема по скаму на відносинах</b>\n\nВ чому суть?\nВ телеграмі є такий бот знайомств дайвінчик - https://t.me/leomatchbot\nЗавдяки йому ми і знаходитимемо орків-мамонтів. Перед тим, як перейти до суті, я розповім усе поверхово. Далі я вже дам усі посилання та усі деталі\nСуть в чому:\n\n1) Ми створюємо лівий тг дівчини. Називаємо її припустимо Софія. Ставимо аватарку, робимо анкету в дайвінчику і чекаємо на лайки.\n\n 2) Коли пішли лайки з бота, ставимо взаємні лайки і тобі друг почнуть писати хлопці з РФ. Мамонти яких ми в'єбем на бабки.\n\n3) Заводиш з ними спілкування і в процесі листування просиш його інсту або вк. Якщо інсти немає, одразу запитуєш. Вилучив? Якщо так, просиш Вк. Інста треба у будь-якому випадку.\n\n4) Як він дав інсту, заходимо. Скриним профіль, всі хто його лайкав, кого він відзначав на фотографіях і сторіс, писав коментарі і т.д. Скриньмо абсолютно все оточення.\n\n5) Зберігаємо його інсту і все, що на скрініли.\n\n6) Якщо немає інсти або вона порожня повністю, кидаємо його в ЧС та шукаємо іншого пацана.\n\n6.1) Якщо він не дає інст і тд, то можете просто випрошувати гроші казати кинь на солодке,кинь на суші,і тд.\n\n7) Далі ми з ним небагато спілкуємось , може виводимо його на інтимні та пошлі повідомлення , та просимо обмінятися інтимними фото\n\n8) Як тільки він скидає член, ви його теж зберігаєте. + робите скріни(якщо ви через інсту то якщо маєте андроїд можете через програмі Instander зберігати даже фотки замість скрінів) переписки, там де він писав вам усе не пристойне.\n\n9) Далі пишіть йому, припустимо: «Хлопець! Що ж ти твориш, мені 15 років і ти потрапив під 134 УКРФ»\n\nСкидаєте відразу після цього смс все що у вас збережено, інсту його знайомих, його член. І пишіть, що пропонуєте знайти компроміс, інакше все розішлете, ніж він займається в інтернеті, так ще й заяву напишіть.\n\n10) Якщо в інсті буде його мати, сестро. Це прямий наш клієнт.\n\nДалі він погоджується на компроміс, кидаєте карту. Просіть 5К рублів або більше/менше. Даєте 5 хвилин щоб скинути. Нема грошей нехай бере позику, що завгодно. Вас не хвилює, у вас його член та знайомі і це ФАКТ! Якщо він вам скинув, далі пишіть. Молодець хлопець, від заяви відкупився, давай ще 5К за злив та розходимося. І так крутимо на максимум. Також як тільки скрини кидаєте, пишіть ще:\n\nЯкщо будеш ігнорити – зілью твої фотки\n\nЯкщо кинеш у чс  - також зілью твої фотки\n\nВидалиш листування – ЗЛИВ, в мене все одно збережена вся наша переписка\n\nЦе вже включайте уяву вашої фантазії та умінь як зробити, щоб він не впав з гачка. Схему думаю зрозуміли, з чого треба розпочати?\n\nДля початку нам треба голі фотки дівчини та звичайні")

            elif m.text == 'Схема по скаму 2':
                bot.send_message(m.chat.id,
                            'Схема по скаму орків «наркота»\n\nЩо для цього потрібно?\n\n1. Ми надаємо вам раш чати по яким будем кидати розсилку\n\n2. Даєм вам розсилку яку потрібно кидати по раш чатах\n\n3. Даємо раш карту на яку буде «нарік» оплачувати товар.\n\n4. Надаємо фотографії товару який «є» в асортименті.\n\n5. Кидаємо вам прайс, потім ви перекидаєте це орку.\n\n6. Обробляєте орка, і все гроші в кармані🤝')

            elif m.text == 'Схема по скаму 3':
                bot.send_message(m.chat.id,
                            'Крч схема для пацанів і для дівчат така:\nДля дівчат по маніку/косметиці,для пацанів по шмотках/якимось товаром, план дій:\n\n1.Робите ви інсту там виставляєте фотки(якшо треба пишіть адміну)\n\n2. Закидуємо відгуки з інших інст акків по маніку/товару, створюємо приємний дизайн. Ваш профіт напряму залежить від того як ви оформите свій аккаунт.\n\n2.Не будуть у нас записуватись на манік якщо в нас буде 3 підписника 😹Тому потрібно накрутити шукайте людей котрі підписані на тематику таку, і кидайте їм запит на стеження,або рекламу, і ставте ціну меншу ніж в всіх і всьо будете мати профіти')

            elif m.text == 'Схема по скаму 4':
                bot.send_message(m.chat.id,
                            'Робимо закриту групу, можна залишити порожньою, але краще накидати "приватних" чи "домашніх" фото, їх море в інтернеті, та ви й самі знаєте. Накрутити до групи близько 100-150 підписників, бажано не більше. Додати опис про "зливи домашніх та приватних фото" та платний вхід.\nНе забудьте, що потрібно купити кілька лівих облікових записів і працювати з них.\nПокрокова інструкція:\n\n1. Створюємо групу ВК, переходимо до пошуку жертв.\n\n2. Такими є молоді дівчата, найкращий варіант 17-20 років, шукаємо їх по молодіжних группах.\n\n3. Пишемо їм наступне (з лівого облікового запису):\n"Привіт, ти начебто не схожа на одну з Цих, фотки яких постійно зливають (вставляємо посилання на групу). Тому хочу тебе попередити, що хтось додав туди твої фотографії. Краще напиши адміністратору, щоб він їх видалив." або "Привіт, я тебе бачив в группі, давай познайомимося? В тебе дуже гарна фігура, мені подобаются твої горячі фоточки), можешь і мені , ще додаткові скинути, бо ті, що в группу мені вже надоїли" вона в вас запитая, що за группа, а ви їй скидуєте посилання.\n\n4. Ймовірно вам будуть ставити запитання, але більше з цього облікового запису не відповідаємо (можете спробувати та поспілкуватися, але я пропоную такий варіант заради економії часу)\n\n5. Розсилаємо таке повідомлення максимально велику кількість людей.\n\n6. Заходимо в обліковий запис адміністрації і бачимо гору повідомлень. Багатьох із їх роз"їсть цікавість і вони сплатять доступ до групи.\nОкрім вк, це можливо зробити і в ті, беріть фантазуйте і робіть! Раджу виставити ціну на вхід не більше ніж 200-300 рублів. (це нормальна сума, бо дівчат, вам буде багато писати і продажів буде норм!)\nСхема дужеее проста, і можна її , ще більш модернізувати. Тому фантазуйте, та робіть великі профіти.')

            elif m.text == 'Схема по скаму 5':
                bot.send_message(m.chat.id,
                            'Будемо скамити руськіх студентів на курсові/дипломні роботи.В кінці схемки закину чати,також можете шукати самі - писати в пошуку назву університета в рашці і чат.\n\nВ чому суть?\n\n1)Шукаємо чат або сайт та пишемо наш шаблоний текст :\n\n📚Делаю студенческие работы📚\n✍🏻Курсовые/дипломные/рефераты/отчеты/решение задач.✍🏻\n💶Делаю быстро и по хорошим ценам🏃\n\n2) Також якщо в чатах хтось пише по типу "Нужно сделать курсовую и т.д" - пишете їм в лс та пропонуєте свої "послуги"\n\n3)Класно буде ще коли ви з іншого аккаунта відповісте на своє повідомлення в чаті і порекомендуєте свій перший акк)) приблизно так "брав у нього курсову всьо збс пройшло - тільки на кацапсткій.)\n\n4)Коли вже кацап написав вам та цікавиться - в нього немає іншого вибору ніж кинути гроші вперед перед виконанням роботи - тому що так роблять всі)\n\nСхемка дуже проста та предоплата не відклякує кацапів.\n\nЧати :\n\nhttps://t.me/kursovaya_diplom\n\nhttps://t.me/chat_msu\n\nhttps://t.me/boilingchat\n\nhttps://t.me/abiturient_itmo\n\nhttps://t.me/abitur_mmspbu\n\nhttps://t.me/abtuz2022')

            elif m.text == 'Схема по скаму 6':
                bot.send_message(m.chat.id,
                            '<b>Мобілізація</b>\n\nСтворюємо фейк тг - « где раздают повестки/Питер/Москва/Мухосранск». Потрібно наповнити канал ? Крадемо пости тут:\n\nhttps://t.me/povestkavmsk\n\nhttps://t.me/viezd_russia\n\nАбо просто пишемо в пошуку Повестки і місто по якому працюєте. Де брати майбутньомогилізованих?\n\n<b>Безкоштовний варіант</b>\n\n1)Пишемо в коменти від імені каналу «У меня информация где раздают повестки» повірте набіжать як бджоли на мед 🐝 \n\n2)Створюєте інст під тг і звідти заганяєте трафік підписуючись на ЦА  (цільову аудиторію )\n\n<b>Платний варіант</b>\n\nБеремо рекламу в кацапських тг каналів з ЦА 25-40 років та заливаємо все в телегу з повістками. Тепер у орків є довіра ( адже ми сливаємо місця де роздають повістки - ми чесні люди ) Тепер впаюємо їм продаж любої хуйні яка їм потрібна : \n\n•Як виїхати з рф якщо ти призивного віку\n\n•фейк сертифікати\n\n•проблеми зі здоров‘ям\n\n•як відкосити від війни')

            elif m.text == 'Схема по скаму 7':
                bot.send_message(m.chat.id,
                            'Всі ми прекрасно знаємо як літом шукали всі приват, і різні карточки, так вот можна так само скамити\n\nПлан дій:\n\n1)Шукаємо руські чати по р2р,заробітку,крипті. Пишемо повідомлення по типу:\n\nСрочно нужен дроп Тинькофф/Сбербанк. С круга плачу 1500. После долгого сотрудничества плачу больше.\n\n2)Кацапи вам самі пишуть в лс - потім ви говорите що вам потрібен їх паспорт та предоплата у розмірі 2500₽ або 5000₽ щоб ви були впевнені що вас не кинуть. Втіраєте ім що вам потрібно дроп на довгий час і якщо все нормально буде то будемо часто «крутити» його картки\nІ все ви забераєте гроші і кидаєте його')

        else:
            bot.send_message(m.chat.id, 'Я можу відповідати лише на повідомлення з меню\nЩо б отримати меню потрібно купити повну версію\nДе купити - @glebmandziy')


bot.polling(none_stop=True)
