# Подключаем библиотеку для работы с статистикой по COVID19
import COVID19Py
# Подключаем Библиотека для работы с АПИ телеграмм
import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

covid19 = COVID19Py.COVID19()
# Указываем токен нашего телеграм-бота
bot = telebot.TeleBot('1816019463:AAELiXN1FALdtVM3MRyGTVMhe5p3FpuhrXA')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('Италия')
	btn2 = types.KeyboardButton('Украина')
	btn3 = types.KeyboardButton('Россия')
	btn4 = types.KeyboardButton('Узбекистан')
	markup.add(btn1, btn2, btn3, btn4)

# Сообщение которое будет отвечать нам бот при  отправки команды /start  
	send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса напишите " \
		f"название страны, например: США, Украина, Россия и так далее\n"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "украина":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "беларусь":
		location = covid19.getLocationByCountryCode("BY")
	elif get_message_bot == "узбекистан":
		location = covid19.getLocationByCountryCode("UZ")
	elif get_message_bot == "уругвай":
		location = covid19.getLocationByCountryCode("UY")
	elif get_message_bot == "италия":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "франция":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "германия":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "япония":
		location = covid19.getLocationByCountryCode("JP")
	else:		   
    	 return bot.send_message(message.chat. id, str("Страна не найдено. Введите страну корректно !!!"))
      

	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[0].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}" \
            f"{location[0]['latest']['recovered']:,}"
				

	bot.send_message(message.chat.id, final_message, parse_mode='html')

# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)


