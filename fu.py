# coding=utf-8

import telebot

bot = telebot.TeleBot('1378253402:AAETP7v9HwTvnzbwP_bIoiTkGoJPksQfsaM')


@bot.message_handler(commands=["start"])
def start_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("I want to watch a film", 'I want to watch a series')
    bot.send_message(message.from_user.id, "Hello, how can I help you?", reply_markup=user_markup)


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(message.from_user.id, "If you want to back to film genres use /back; ig you want to back to "
                                           "series genres use /backs")


@bot.message_handler(commands=["back"])
def back_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('comedy', 'horror', 'thriller')
    user_markup.row('animation', 'romance', 'sci-fi')
    bot.send_message(message.from_user.id, "What film genre do you prefer?", reply_markup=user_markup)
    bot.register_next_step_handler(message, genre)


@bot.message_handler(commands=["backs"])
def backs_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('comedy', 'horror', 'thriller')
    user_markup.row('fantasy', 'Netflix', 'russian series')
    bot.send_message(message.from_user.id, "Which series do you prefer?", reply_markup=user_markup)
    bot.register_next_step_handler(message, genres)


@bot.message_handler(commands=["stop"])
def start_command(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Goodbye! Have a nice day!", reply_markup=hide_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "I want to watch a film":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('comedy', 'horror', 'thriller')
        user_markup.row('animation', 'romance', 'sci-fi')
        bot.send_message(message.from_user.id, "What film genre do you prefer?", reply_markup=user_markup)
        bot.register_next_step_handler(message, genre)
    elif message.text == "I want to watch a series":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('comedy', 'horror', 'thriller')
        user_markup.row('fantasy', 'Netflix', 'russian series')
        bot.send_message(message.from_user.id, "Which series do you prefer?", reply_markup=user_markup)
        bot.register_next_step_handler(message, genres)


def genres(message):
    if message.text == "comedy":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Friends')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you a series:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    if message.text == "horror":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('American Horror Story')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you a series:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    if message.text == "thriller":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Stranger Things')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you a series:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    if message.text == "fantasy":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Game of Thrones')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you a series:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Netflix":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Black Mirror')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you a series:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    if message.text == "russian series":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Kitchen')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you a series:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)


def genre(message):
    if message.text == "comedy":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Always Be My Maybe', 'Hustlers', 'Good Boys')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you some films:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    elif message.text == "horror":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('THE RING', 'DOG SOLDIERS', 'OCULUS')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you some films:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    elif message.text == "thriller":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('47 Meters Down', '1922', 'American Psycho')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you some films:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    elif message.text == "animation":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Paddington', 'Toy Story', 'How to Train Your Dragon')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you some films:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    elif message.text == "romance":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Moulin Rouge!', 'The Notebook', 'About Time')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you some films:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)
    elif message.text == "sci-fi":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('War of the Worlds', 'Moon', 'Inception')
        bot.send_message(message.from_user.id, "It`s a great choice! I can recommend you some films:",
                         reply_markup=user_markup)
        bot.register_next_step_handler(message, url)


@bot.message_handler(commands=['url'])
def url(message):
    markup = telebot.types.InlineKeyboardMarkup()
    if message.text == "Always Be My Maybe":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://filmix.co/melodramy/133957-ty-moe-somnenie-2019.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Hustlers":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://kinohold.club/32507-striptizershi-2019-hd4.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Good Boys":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://kinob.net/film/36402-horoshie-malchiki')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "THE RING":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/detektivy/2800-zvonok.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "DOG SOLDIERS":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/boeviki/3318-psy-voiny.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "OCULUS":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/trillery/9732-okulus.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "47 Meters Down":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://rezka.ag/films/horror/17875-sinyaya-bezdna-2017.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "1922":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://rezka.ag/films/drama/25891-1922-2017.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "American Psycho":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://rezka.ag/films/drama/3033-amerikanskiy-psihopat-2000.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Paddington":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://kinokrad.co/267130-priklyucheniyya-paddingtona-2015-hdtv.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Toy Story":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://kinokrad.co/281733-istoriya-igrushek.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "How to Train Your Dragon":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/komedii/197-kak-priruchit-drakona.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Moulin Rouge!":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://rezka.ag/films/drama/4434-mulen-ruzh-2001.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "The Notebook":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/dramy/632-dnevnik-pamyati.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "About Time":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://rezka.ag/films/fiction/917-boyfrend-iz-buduschego-2013.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "War of the Worlds":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/boeviki/2830-voyna-mirov.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Moon":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='https://rezka.ag/films/fiction/5744-luna-2112-2009.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Inception":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the film",
                                                         url='http://baskino.me/films/boeviki/105-nachalo.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the film", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Friends":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the series",
                                                         url='http://friends-online.co/')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the series", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "American Horror Story":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the series",
                                                         url='https://hdrezka-ag.com/series/horror/233-amerikanskaya-istoriya-uzhasov-2011.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the series", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Stranger Things":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the series",
                                                         url='https://hdrezka-ag.com/series/thriller/17109-ochen-strannye-dela-2016.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the series", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Game of Thrones":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the series",
                                                         url='https://hdrezka-ag.com/series/fantasy/45-igra-prestolov-2011-tv-series-1.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the series", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Black Mirror":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the series",
                                                         url='https://hdrezka-ag.com/series/fiction/77-chernoe-zerkalo-2011.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the series", reply_markup=markup)
        bot.register_next_step_handler(message, url)
    if message.text == "Kitchen":
        btn_my_site = telebot.types.InlineKeyboardButton(text="Watch the series",
                                                         url='https://hdrezka-ag.com/series/comedy/1404-kuhnya-2012.html')
        markup.add(btn_my_site)
        bot.send_message(message.chat.id, "Press the button to watch the series", reply_markup=markup)
        bot.register_next_step_handler(message, url)


if __name__ == '__main__':
    bot.polling(none_stop=True)