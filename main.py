## ------------------------- Импорты ------------------------- ##
from vkbottle.bot import Bot, Message
from config import token


## ------------------------- Переменные ------------------------- ##
bot = Bot(token)
bot.labeler.vbml_ignore_case = True


## ------------------------- Реакции на сообщения ------------------------- ##
@bot.on.chat_message(text=["привет", "hello", "hi", "ку", "qq", "q", "хай", "дарова", "здравствуй", "доброго времени суток", "вечер в хату", "здравствуйте", "здарова", "пиривирет", "приветик", "приветули", "алоха", "пиривет"])
async def message_handler(message: Message):
    user = await bot.api.users.get(message.from_id)
    if user[0].first_name == "Артём":
        if user[0].last_name == "Чикинов":
            await message.reply(f"Привет, мой любимый Тёмочка❤")
        else:
            await message.reply(f"Привет, {user[0].first_name}❤")
    elif user[0].first_name == "Artem":
            await message.reply(f"Привет, Артём❤")
    elif user[0].first_name == "Игорь":
            if user[0].last_name == "Носков":
                await message.reply(f"Привет, Иго... урод💢 Это я машина? Это у меня нет души?")
            else:
               await message.reply(f"Привет, {user[0].first_name}❤") 
    else:
        await message.reply(f"Привет, {user[0].first_name}❤")


## ------------------------- Запуск бота ------------------------- ##
bot.run_forever()