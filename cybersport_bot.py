from aiogram import Bot, Dispatcher, executor, types
import logging
import json



token = "5141075916:AAEb_isM5emJPxk9L3f551Ek9NR0ROd4qB8"

bot = Bot(token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

with open("matches.json", "r") as file:
    all_matches = json.load(file)

def get_media_group(counter):

    media_group = types.MediaGroup()

    media_group.attach_photo(
        types.InputFile(f"C:/Users/875l/PycharmProjects/parsing/icons/{all_matches[counter]['team_name_left']}.jpg"),
        all_matches[counter]['datetime'] + "\n" + all_matches[counter]['team_name_left'] + " VS " + all_matches[counter]['team_name_right'] + "\n" * 2 + "Ссылка на матч: " + all_matches[0]['match_href'])

    media_group.attach_photo(
        types.InputFile(f"C:/Users/875l/PycharmProjects/parsing/icons/{all_matches[counter]['team_name_right']}.jpg"))

    return media_group


@dp.message_handler(commands="start")
async def start(message: types.Message):

    start_buttons = ["Ближайший матч", "10 Ближайших матчей", "Все матчи на сегодня"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Привет, я бот по Доте", reply_markup=keyboard)



@dp.message_handler(commands="info")
async def start(message: types.Message):
    await message.answer("Бот ещё в разработке")



@dp.message_handler(content_types=['text'])
async def test(message: types.Message):

    text = message.text
    chatId = message.chat.id

    if text == "Ближайший матч":

        await bot.send_media_group(chatId, media=get_media_group(0))



    if text == "10 Ближайших матчей":

        counter = 0

        while counter < 10:
            await bot.send_media_group(chatId, media=get_media_group(counter))
            counter += 1



    if text == "Все матчи на сегодня":

        cur_day = all_matches[0]['datetime'][:2]

        counter = 0
        while cur_day == all_matches[counter]['datetime'][:2]:

            await bot.send_media_group(chatId, media=get_media_group(counter))

            counter += 1



if __name__ == '__main__':
    executor.start_polling(dp)

