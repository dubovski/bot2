import telebot
import pyowm
def main():

	owm = pyowm.OWM('e0075e455bf151fc202115c37adb8ef3')
	bot = telebot.TeleBot("804486158:AAGAmxc7FMI-XFl3uxQUTfjP2yg9a0NBOOA")

	@bot.message_handler(content_types=['text'])
	def send_welcome(message):
		try:
			observation = owm.weather_at_place(message.text)
			w = observation.get_weather()
			z = w.get_temperature('celsius')["temp"]
			answer = "V gorode  " + str(message.text) + " seichas  " + str(z) + "  gradusov  " + "\n\n"
			if z >= 14:
				answer += "Nafig Kurtku"
			else:
				answer += "Naden Kurtku11"

			bot.send_message(message.chat.id, answer)
		except pyowm.exceptions.api_response_error.NotFoundError:
			answer = "Cho za gorod?"
			bot.send_message(message.chat.id, answer)

	# @bot.message_handler(func=lambda message: True)
	# def echo_all(message):
	#	bot.reply_to(message, message.text)

	bot.polling()


if __name__ == '__main__':
	main()