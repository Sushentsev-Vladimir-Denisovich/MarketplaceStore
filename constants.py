# Базовые сообщения
welcome_message = "Здравствуйте!\n\nЯ бот онлайн магазина «DwellWell». Пожалуйста, выберите, чем я могу вам помочь.";
not_user_id = "Некому отправить сообщение(";
incorrect_user_id = "Неверно введен ID пользователя!";
wait_start = "Напиши /start";
start = "/start";
question_message = "Пожалуйста, задайте мне свой вопрос. Я отправлю его менеджеру и перешлю ответ";
order_nuber_message = "Пожалуйста, напишите номер заказа, с которым возникла проблема.";
problem_message = "Спасибо!\n\nОпишите, пожалуйста, возникшую проблему. Я отправлю её менеджеру и перешлю ответ";
wait_number = "Цифрами, пожалуйста";

# Константы для кнопок на клавиатуре
keyboard_question = "Вопрос о товаре";
keyboard_problem = "Проблема с товаром";
keyboard_OZON_name = "Мы на OZON";
keyboard_OZON_URL = "https://ozon.ru/t/d003na8";
keyboard_WB_name = "Мы на Wildberries";
keyboard_WB_URL = "";
keyboard_back = "Вернуться в главное меню";

# Наименования callback-ов
clbk_question = "question";
clbk_problem = "problem";
clbk_ozon = "ozon";
clbk_wb = "wb";
clbk_back = "back";

# Разделитель
delimeter = "%";

# Массив стикеров для генерации рандомного
stickers = ['CAACAgIAAxkBAAEMYdBmfNw1Hj2kwDyaOxC2NdUm8ZpNiQACtRUAAkpCIUo1moL1RhkEsTUE', 'CAACAgIAAxkBAAEMYdRmfNziiLSejnTyPHYRpra_fB6Q1QACOiAAAh2ysUhE-eo7-iAe7zUE',
         'CAACAgIAAxkBAAEMYdZmfNzm_dWVBygTn24cSK9-ipFoZQACNBYAAraSQEpMkl93t5zXXjUE', 'CAACAgIAAxkBAAEMYdhmfNzpdJ_9m6JrJJ2Gy4IB9ioGlgACNxYAAq4fIUobMLLOfGdb9TUE',
         'CAACAgIAAxkBAAEMYdpmfN0TUoDqbqZoL3-tnZRq0cLljQACrhgAAvwNOEoNJAoAAanMwlc1BA', 'CAACAgIAAxkBAAEMYdxmfN0oWSOdo1FV2rHxIwrE8Iq5dQAC0hQAAt2QKUqCwaVZrdHnJzUE',
         'CAACAgIAAxkBAAEMYd5mfN04h--A_6YknN1iWg6hoobgXAACERYAAqtFKErwJjajc6owvDUE', 'CAACAgIAAxkBAAEMYeBmfN1E17CgUgckslEIbAABjY1WTYUAAlAYAAKGvzhKp7Ne272vD-E1BA',
         'CAACAgIAAxkBAAEMYeJmfN1HTdnM0TCrgO9bJ5_pbp5NSwACyBoAAmQEOUr6whBlsxtpHTUE', 'CAACAgIAAxkBAAEMYeRmfN1Jm9-G0Z6OJH5FKsm4nvf1NAACUBUAAt00QEoOc00Yz2TuHzUE',
         'CAACAgIAAxkBAAEMYeZmfN1h9DPukBfVbQzIdwc5EaiCcgACcxYAAkHFOUqAFPojtRfCUDUE', 'CAACAgIAAxkBAAEMYehmfN1m3GVshFLE39ZLzhiV2A0gfAACIxkAAsXhOErxPO4MxFczsjUE',
         'CAACAgIAAxkBAAEMYepmfN1oQG1ynXBHEmOMY8ntBIHBbwACixcAArJYOEoXjHpxHO5OeDUE', 'CAACAgIAAxkBAAEMYexmfN19q6qphea8qvI7sdsDK9AeOQACZxQAAloAASBKrIOiKs94Q841BA',
         'CAACAgIAAxkBAAEMYe5mfN3tCM4diXXhazXqJ5Uo6_ZtrwACBBUAAnrwQEpGmLybrR9udzUE', 'CAACAgIAAxkBAAEMYfBmfN4Gr46AvZsb_OkD2Y2kM8WmNAACxBsAAuooOUroqTj1XeGdMjUE',
         'CAACAgIAAxkBAAEMYfJmfN4RD-7AvyE0rlLBvsEp4KVi7wACIC4AAr3I4Uu0jRzVoxnItDUE', 'CAACAgIAAxkBAAEMYfRmfN4iU_D-rY_Ls0Nes0wKITf8VAACfiIAApbiiEv_T6l11Dku5TUE',
         'CAACAgIAAxkBAAEMYfZmfN4kAimCk21nBjfWagfFZTGawQAC_CgAAmh04UsAAU012dlo8zc1BA', 'CAACAgIAAxkBAAEMYfdmfN4my52w6OOWeFP8rC76eYBV-AACJS8AAo4b6Uv3h5EhK4qavDUE',
         'CAACAgIAAxkBAAEMYflmfN4pfMIPOB65u-jqoDBAjqBjsgACox0AArz3mUlCtbhCaeztAzUE', 'CAACAgIAAxkBAAEMYfxmfN4rhLQ4Yfqb3WqQWnOMmvawLwAC3DEAAlGEmEtRO_vPO2OHIzUE',
         'CAACAgIAAxkBAAEMYf5mfN4y9oquWT8aFk_jM9MvCJFeFwACux4AAkz_-UgAAfzSBvSG9Ik1BA', 'CAACAgIAAxkBAAEMYgABZnzeNIt9SAWF4R7IoziPW7pzNzgAAg0VAAKDUdlLxdu9zCyBbJE1BA',
         'CAACAgIAAxkBAAEMYgJmfN44P-tKNnAgT91mjjx7xaBX_gACJy4AAlg04Et2XfhWzbJwHTUE', 'CAACAgIAAxkBAAEMYgRmfN6KjMbMmhqBu2vkEeSM694t0wACBkAAAls1iUt2Zs2y4gPaIjUE',
         'CAACAgIAAxkBAAEMYgVmfN6LNQXkoCe1xE4AAce3s9S1G_kAAoA-AAKN6IlLPpTs4irKdUQ1BA', 'CAACAgIAAxkBAAEMYgZmfN6MBsaQ0egSapZAZGxWa8KAMAACZz8AArqDiUvF9f06xjNdfzUE',
         'CAACAgIAAxkBAAEMYgdmfN6Mbz0qpoHkD0HnghZ_D7vLmQACOz4AArKYiUtkdlTPASQyjzUE', 'CAACAgIAAxkBAAEMYglmfN6NRVqXovgi5OQBP6oTtabTHAACZj4AAhOaiEtR5jbGfS20LDUE',
         'CAACAgIAAxkBAAEMYgpmfN6NcrC8qqPsu1_0VUUtgrRHDAACgDYAAtxaiEtR8i1oOv-rBTUE', 'CAACAgIAAxkBAAEMYgtmfN6NFfmVceqIY_UsrB2nrVtrSAACE0QAAoYQiEvNzkAjOVWWmzUE',
         'CAACAgIAAxkBAAEMYg1mfN6OpCg7Z3JN4pNR1qAUKZWmDgACrzsAAqqWiEuhc2pZP5CrRjUE', 'CAACAgIAAxkBAAEMYg5mfN6PAV5YItSDjUG2pSr1-nkpIQAC2T8AAqdPiEsblVfCrBx4MzUE',
         'CAACAgIAAxkBAAEMYg9mfN6PRBoTTOKCc23EmKXm3ugpUAAC50EAAi9IgEuuLZ9tP20o1jUE', 'CAACAgIAAxkBAAEMYhBmfN6QgrLoQqh8RZo3Kl2FF7IxVwACcjQAAvIJiEtpmUYdhW4aFzUE'] 