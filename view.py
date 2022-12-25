from bot import bot


async def start_game(message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}\n'
                                                 f'Правила игры: '
                                                 f' На столе лежит 117 конфет.'
                                                 f' Играют два игрока делая ход друг после друга.'
                                                 f' Первый ход определяется жеребьёвкой.'
                                                 f' За один ход можно забрать не более чем 28 конфет.'
                                                 f' Все конфеты оппонента достаются сделавшему последний ход.')


async def player_take(message):
    await bot.send_message(message.from_user.id, f'Возьмите конфеты, но не больше 28 конфет: ')


async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет,\n '
                                                 f'на столе осталось {total_count} конфет '
                                                 f'Ходит {name2}')


async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id, f'{name} взял {take} конфет,\n '
                                                 f'на столе осталось {total_count} конфет '
                                                 f'{name} победил!')


async def wrong_take(message):
    await bot.send_message(message.from_user.id, f'Вы взяли слишком много конфет, попробуйте снова!')