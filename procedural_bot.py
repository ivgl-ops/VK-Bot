#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random


from Sourse import openfile
from Sourse import randomrecipe

#login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()

token ='b825ac119d519d3ef793244c05ea4866a5290832e3ea72448b73004e0fc587486848649a1db8dfbe3213a'

vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
fav_list = []
print("Бот запущен")


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    if response == 'функции':
        keyboard.add_button('Категории', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Рандомный рецепт', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Подобрать блюдо', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Поиск по каллориям', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Избранное', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Начать', color=VkKeyboardColor.NEGATIVE)

    elif response == 'начать':
        keyboard.add_button('Функции', color=VkKeyboardColor.DEFAULT)


    elif response == 'поиск по каллориям':
        keyboard.add_button('500+ ккал', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('200 - 400 ккал', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('100 - 200 ккал', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Функции', color=VkKeyboardColor.DEFAULT)

    elif response == '500+ ккал':
        keyboard.add_button('Бефстроганов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Голубцы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Гуляш', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Лагман', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Отбивная из курицы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Запеканка мясная', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('поиск по каллориям', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('далее 500+', color=VkKeyboardColor.PRIMARY)

    elif response == "далее 500+":
        keyboard.add_button('Шаурма с курицей', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мини-слойки с курицей', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('500+ ккал', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('поиск по каллориям', color=VkKeyboardColor.DEFAULT)

    elif response == '200 - 300 ккал':
        keyboard.add_button('Пицца', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пончики', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Леденцы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Блины', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Печенье Oreo', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Капкейки', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('поиск по каллориям', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('далее 200 - 300 ккал', color=VkKeyboardColor.PRIMARY)

    elif response == 'далее 200 - 300 ккал':
        keyboard.add_button('Паста карбонара', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Джамбалайя', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Плов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Картофель тушёный', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('200 - 300 ккал', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('поиск по каллориям', color=VkKeyboardColor.DEFAULT)

    elif response == '100 - 200 ккал':
        keyboard.add_button('Салат с креветками и кунжутом', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Английский салат', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Салат с курицей в азиатском стиле', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Салат с сыром и курицей', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Леденцы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Борщ', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('поиск по каллориям', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Далее 100 - 200 ккал', color=VkKeyboardColor.PRIMARY)

    elif response ==  'далее 100 - 200 ккал':
        keyboard.add_button('Сырный суп', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Грибной суп', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Шурпа', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Уха', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Суп с фрикадельками', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Рассольник', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('100 - 200 ккал', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('поиск по каллориям', color=VkKeyboardColor.DEFAULT)

    elif response == 'категории':
        keyboard.add_button('Выпечка', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Сладости', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Салаты', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Закуски', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)


    elif response == 'салаты':
        keyboard.add_button('Салат с креветками и кунжутом', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Английский салат', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Салат с курицей в азиатском стиле', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Салат с сыром и курицей', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Салат Цезарь', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Кубинский салат', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Еще салаты', color=VkKeyboardColor.NEGATIVE)

    elif response == 'салат цезарь':
        keyboard.add_button('Салаты', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Добавить в избранное салат цезарь', color=VkKeyboardColor.PRIMARY)

    elif response == 'английский салат':
        keyboard.add_button('Добавить в избранное английский салат', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Салаты', color=VkKeyboardColor.DEFAULT)
    elif response == '':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('', color=VkKeyboardColor.DEFAULT)

    elif response == 'пицца':
        keyboard.add_button('Добавить в избранное: ' + response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'хачапури по-аджарски':
        keyboard.add_button('В избранное: '+ response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'пироги печеные':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'осетинский пирог':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'самса с мясом':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'маффины':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'чебуреки':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'пирог зебра':
        keyboard.add_button('Добавить в избранное: '+response.title(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'шарлотка':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'пирог с капустой':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'борщ':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'щи':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'куриный суп с вермишелью':
        keyboard.add_button('В избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'солянка':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'шурпа':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'уха':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'суп с фрикадельками':
        keyboard.add_button('В избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'рассольник':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'сырный суп':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'грибной суп':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)


    elif response == 'бефстроганов':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'голубцы':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'гуляш':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'лагман':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'плов':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'картофель тушёный':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'отбивная из курицы':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'запеканка мясная':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'паста карбонара':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
    elif response == 'джамбалайя':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)


    elif response == '':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('', color=VkKeyboardColor.DEFAULT)

    elif response == 'пицца':
        keyboard.add_button('Добавить в избранное: ' + response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'хачапури по-аджарски':
        keyboard.add_button('В избранное: '+ response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'пироги печеные':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'осетинский пирог':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'самса с мясом':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)
    elif response == 'маффины':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'чебуреки':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'пирог зебра':
        keyboard.add_button('Добавить в избранное: '+response.title(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'шарлотка':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'пирог с капустой':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Выпечка', color=VkKeyboardColor.DEFAULT)

    elif response == 'борщ':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'щи':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'куриный суп с вермишелью':
        keyboard.add_button('В избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'солянка':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'шурпа':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'уха':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'суп с фрикадельками':
        keyboard.add_button('В избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'рассольник':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'сырный суп':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'грибной суп':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT)


    elif response == 'бефстроганов':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'голубцы':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'гуляш':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'лагман':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'плов':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'картофель тушёный':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'отбивная из курицы':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'запеканка мясная':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)

    elif response == 'паста карбонара':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)
        
    elif response == 'джамбалайя':
        keyboard.add_button('Добавить в избранное: '+response.capitalize(), color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT)



    elif response == 'сладости':
        keyboard.add_button('Мармелад',color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пончики', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Леденцы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Блины', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Печенье Oreo', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Капкейки', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Еще сладости', color=VkKeyboardColor.NEGATIVE)

    elif response == 'первые блюда':
        keyboard.add_button('Борщ', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Щи', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Куриный суп с вермишелью', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Солянка', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Шурпа', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Уха', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('категории', color=VkKeyboardColor.NEGATIVE )
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Первые блюда(2/2)', color=VkKeyboardColor.NEGATIVE)

    elif response == 'первые блюда(2/2)':
        keyboard.add_button('Суп с фрикадельками', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Рассольник', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Сырный суп', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Грибной суп', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.NEGATIVE)

    elif response == 'вторые блюда':
        keyboard.add_button('Бефстроганов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Голубцы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Гуляш', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Лагман', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Плов', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Картофель тушёный', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Вторые блюда(2/2)', color=VkKeyboardColor.NEGATIVE)

    elif response == 'вторые блюда(2/2)':
        keyboard.add_button('Отбивная из курицы', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Запеканка мясная', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Паста карбонара', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Джамбалайя', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.NEGATIVE)


    elif response == 'выпечка':
        keyboard.add_button('Пицца', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Хачапури по-аджарски', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Пироги печеные', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Осетинский пирог', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Самса с мясом', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Маффины', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Выпечка (2/2)', color=VkKeyboardColor.NEGATIVE)

    elif response == 'выпечка (2/2)':
        keyboard.add_button('Чебуреки', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пирог Зебра', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Шарлотка', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пирог с капустой', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_line()
        keyboard.add_button('Самса с мясом', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Маффины', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Выпечка (2/2)', color=VkKeyboardColor.NEGATIVE)

    elif response == 'выпечка (2/2)':
        keyboard.add_button('Чебуреки', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пирог Зебра', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Шарлотка', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пирог с капустой', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        keyboard.add_button('категории', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Выпечка', color=VkKeyboardColor.NEGATIVE)

    elif response == 'закуски':
        keyboard.add_button('Шаурма с курицей', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Мини-слойки с курицей', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Функции', color=VkKeyboardColor.NEGATIVE)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()
    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message=None, keyboard=None, attachment=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648),
                                       'keyboard': keyboard, 'attachment': attachment })



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "начать":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)
            elif response == "избранное":
                if len(fav_list) == 0:
                    send_message(vk_session, 'user_id', event.user_id, message='Вы пока что ничего не добавили')
                else:
                    send_message(vk_session, 'user_id', event.user_id, message= 'Избранные рецепты:')
                    for i in fav_list:
                        recipe = i
                        send_message(vk_session, 'user_id', event.user_id, message=i)


            elif response == 'подобрать блюдо':
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('Main_Recipes'))


            elif response == 'добавить в избранное салат цезарь':
                fav_list.append('Салат Цезарь')
                send_message(vk_session, 'user_id', event.user_id, message='рецепт добавлен')

            elif response == 'добавить в избранное английский салат':
                fav_list.append('Английский салат')
                send_message(vk_session, 'user_id', event.user_id, message='рецепт добавлен')


            elif response.find('добавить в избранное: ') != -1 or response.find("в избранное: ") != -1:
                splitstring = response.split(': ')
                fav_list.append(splitstring[1])
                send_message(vk_session, 'user_id', event.user_id, message='рецепт добавлен')

            elif response == "500+ ккал":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт', keyboard=keyboard)
            elif response == "далее 500+":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт', keyboard=keyboard)
            elif response == "далее 200 - 300 ккал":
              send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт',keyboard=keyboard)
            elif response == "200 - 300 ккал":
              send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт',keyboard=keyboard)
            elif response == "100 - 200 ккал":
              send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт',keyboard=keyboard)
            elif response == "далее 100 - 200 ккал":
              send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт',keyboard=keyboard)
            elif response == "~300 ккал":
              send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт',keyboard=keyboard)
            elif response == "поиск по каллориям":
              send_message(vk_session, 'user_id', event.user_id, message='Выберите нужный пункт',keyboard=keyboard)
            elif response == "шаурма с курицей":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/shaurma'),
                           attachment='photo-194978607_457239033')
              fav_list.append('шаурма с курицей')
            elif response == "мини-слойки с курицей":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/mini_sloyki'),
                             attachment='photo-194978607_457239034')
            elif response == "печенье oreo":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/cookie'),
                           attachment='photo-194978607_457239022')
            elif response == "салат цезарь":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/salad_Cesar'),
                           attachment='photo-194978607_457239028', keyboard=keyboard)
            elif response == "кубинский салат":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/salad_cuba'),
                           attachment='photo-194978607_457239030')
            elif response == "салат с сыром и курицей":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/salad_with_cheese'),
                           attachment='photo-194978607_457239027')
            elif response == "салат с курицей в азиатском стиле":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/salad_with_checken'),
                           attachment='photo-194978607_457239026')
            elif response == "капкейки":
              send_message(vk_session, 'user_id', event.user_id,message = openfile.open_in('recipes/cupcake'),
                           attachment='photo-194978607_457239023')
            elif response == "блины":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/pancake'),
                           attachment='photo-194978607_457239021')


            elif response == "борщ":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Borch.TXT'),
                           attachment='photo-194978607_457239046', keyboard=keyboard)
            elif response == "щи":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Chi.TXT'),
                           attachment='photo-194978607_457239047', keyboard=keyboard)
            elif response == "грибной суп":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Gribnoy_soup.TXT'),
                           attachment='photo-194978607_457239045', keyboard=keyboard)
            elif response == "уха":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Yuha.TXT'),
                           attachment='photo-194978607_457239050', keyboard=keyboard)
            elif response == "сырный суп":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Cheeze_soup.TXT'),
                           attachment='photo-194978607_457239049', keyboard=keyboard)
            elif response == "солянка":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Solyanka.TXT'),
                           attachment='photo-194978607_457239052', keyboard=keyboard)
            elif response == "рассольник":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Rassolnik.TXT'),
                           attachment='photo-194978607_457239051', keyboard=keyboard)
            elif response == "шурпа":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Shurpa.TXT'),
                           attachment='photo-194978607_457239048', keyboard=keyboard)
            elif response == "суп с фрикадельками":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Soup_with_frikadelki.TXT'),
                           attachment='photo-194978607_457239053', keyboard=keyboard)
            elif response == "куриный суп с вермишелью":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\pfirst_food\Kuriniy_soup_with_vermishel.TXT'),
                           attachment='photo-194978607_457239054', keyboard=keyboard)


            elif response == "бефстроганов":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Befstroganov.TXT'),
                           attachment='photo-194978607_457239061', keyboard=keyboard)
            elif response == "голубцы":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Golubcy.TXT'),
                           attachment='photo-194978607_457239063', keyboard=keyboard)
            elif response == "плов":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Plov.TXT'),
                           attachment='photo-194978607_457239059', keyboard=keyboard)
            elif response == "гуляш":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Gulyash.TXT'),
                           attachment='photo-194978607_457239056', keyboard=keyboard)
            elif response == "отбивная из курицы":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Otbivhie_iz_kurici.TXT'),
                           attachment='photo-194978607_457239064', keyboard=keyboard)
            elif response == "паста карбонара":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Pasta_Karbonara.TXT'),
                           attachment='photo-194978607_457239058', keyboard=keyboard)
            elif response == "запеканка мясная":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Zapekanka.TXT'),
                           attachment='photo-194978607_457239057', keyboard=keyboard)
            elif response == "лагман":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Lagman.TXT'),
                           attachment='photo-194978607_457239060', keyboard=keyboard)
            elif response == "картофель тушёный":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Kartofel_tusheniy.TXT'),
                           attachment='photo-194978607_457239055', keyboard=keyboard)
            elif response == "джамбалайя":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes\second_food\Jambalaya.TXT'),
                           attachment='photo-194978607_457239062', keyboard=keyboard)


            elif response == "пицца":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/pizza.TXT'),
                         attachment='photo-194978607_457239041', keyboard=keyboard)
            elif response == "хачапури по-аджарски":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/hachapury.TXT'),
                         attachment='photo-194978607_457239036', keyboard=keyboard)
            elif response == "пироги печеные":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/pirogipechenie.TXT'),
                         attachment='photo-194978607_457239039', keyboard=keyboard)
            elif response == "осетинский пирог":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/osetinskiy.TXT'),
                             attachment='photo-194978607_457239038', keyboard=keyboard)
            elif response == "самса с мясом":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/samsa.TXT'),
                             attachment='photo-194978607_457239042', keyboard=keyboard)
            elif response == "маффины":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/maffins.TXT'),
                             attachment='photo-194978607_457239037', keyboard=keyboard)
            elif response == "чебуреки":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/cheburek.TXT'),
                             attachment='photo-194978607_457239035', keyboard=keyboard)
            elif response == 'пирог зебра':
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/pirogzebra.TXT'),
                             attachment='photo-194978607_457239044', keyboard=keyboard)
            elif response == "шарлотка":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/yablochniypirog.TXT'),
                             attachment='photo-194978607_457239043', keyboard=keyboard)
            elif response == "пирог с капустой":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/pastry/pirogskapustoy.TXT'),
                             attachment='photo-194978607_457239040', keyboard=keyboard)

            elif response == "английский салат":
                send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/eng_salad'),
                       attachment='photo-194978607_457239025', keyboard=keyboard)
            elif response == "салат с креветками и кунжутом":
              send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/salad_with_krevetky'),
                           attachment='photo-194978607_457239024')
            elif response == "салаты":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите салат',keyboard=keyboard)
            elif response == "пончики":
                send_message(vk_session, 'user_id', event.user_id, message= openfile.open_in('recipes/Donat'),
                             attachment='photo-194978607_457239019')
            elif response == "леденцы":
                send_message(vk_session, 'user_id', event.user_id, message= openfile.open_in('recipes/Chupa'),
                             attachment='photo-194978607_457239020')
            elif response == "первые блюда(2/2)":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите первое блюдо', keyboard=keyboard)
            elif response == "вторые блюда(2/2)":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите второе блюдо', keyboard=keyboard)
            elif response == "первые блюда":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите первое блюдо',keyboard=keyboard)
            elif response == "вторые блюда":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите второе блюдо', keyboard=keyboard)
            elif response == "функции":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите нужные команды',keyboard=keyboard)
            elif response == "закуски":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите рецепты',keyboard=keyboard)
            elif response == "категории":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите категорию продукта',keyboard=keyboard)
            elif response == "сладости":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите блюдо',keyboard=keyboard)
            elif response == "выпечка":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите блюдо',keyboard=keyboard)
            elif response == "выпечка (2/2)":
                send_message(vk_session, 'user_id', event.user_id, message= 'Выберите блюдо',keyboard=keyboard)
            elif response == "мармелад":
                send_message(vk_session, 'user_id', event.user_id, message= openfile.open_in('recipes/Marmelade'), attachment='photo-194978607_457239017')

            elif response == 'закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)
                #сделать тут карусель
            #elif response == "подборка самых вкусных рецептов":
                #send_message(vk_session, 'user_id', event.user_id, message=corousel)
                #подумать над логикой рандома


            elif response == "рандомный рецепт":
                response = randomrecipe.random_recipe()
                if response == "мармелад":
                    send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/Marmelade'),
                                attachment='photo-194978607_457239017')

                    # Выпечка (для рандома):
                elif response == "пицца":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/pizza.TXT'),
                                 attachment='photo-194978607_457239041')
                elif response == "хачапури по-аджарски":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/hachapury.TXT'),
                                 attachment='photo-194978607_457239036')
                elif response == "пироги печеные":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/pirogipechenie.TXT'),
                                 attachment='photo-194978607_457239039')
                elif response == "осетинский пирог":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/osetinskiy.TXT'),
                                 attachment='photo-194978607_457239038')
                elif response == "самса с мясом":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/samsa.TXT'),
                                 attachment='photo-194978607_457239042')
                elif response == "маффины":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/maffins.TXT'),
                                 attachment='photo-194978607_457239037')
                elif response == "чебуреки":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/cheburek.TXT'),
                                 attachment='photo-194978607_457239035')
                elif response == 'пирог зебра':
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/pirogzebra.TXT'),
                                 attachment='photo-194978607_457239044')

                elif response == "шарлотка":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/yablochniypirog.TXT'),
                                 attachment='photo-194978607_457239043')
                elif response == "пирог с капустой":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/pastry/pirogskapustoy.TXT'),
                                 attachment='photo-194978607_457239040')


                elif response == "пончики":
                    send_message(vk_session, 'user_id', event.user_id, message= openfile.open_in('recipes/Donat'),
                                 attachment='photo-194978607_457239019')
                elif response == "леденцы":
                    send_message(vk_session, 'user_id', event.user_id, message= openfile.open_in('recipes/Chupa'),
                                 attachment='photo-194978607_457239020')
                elif response == "блины":
                  send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/pancake'),
                               attachment='photo-194978607_457239021')
                elif response == "печенье oreo":
                  send_message(vk_session, 'user_id', event.user_id, message = openfile.open_in('recipes/cookie'),
                               attachment='photo-194978607_457239022')

                elif response == "капкейки":
                    send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/cupcake'),
                                 attachment='photo-194978607_457239023')
                elif response == "салат с креветками и кунжутом":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/salad_with_krevetky'),
                                 attachment='photo-194978607_457239024')
                elif response == "английский салат":
                    send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/eng_salad'),
                                 attachment='photo-194978607_457239025')
                elif response == "салат с курицей в азиатском стиле":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/salad_with_checken'),
                                 attachment='photo-194978607_457239026')
                elif response == "салат с сыром и курицей":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes/salad_with_cheese'),
                                 attachment='photo-194978607_457239027')
                elif response == "салат цезарь":
                    send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/salad_Cesar'),
                                 attachment='photo-194978607_457239028')
                elif response == "кубинский салат":
                    send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/salad_cuba'),
                                 attachment='photo-194978607_457239030')

                    # Первые блюда (для рандома):
                elif response == "борщ":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Borch.TXT'),
                                 attachment='photo-194978607_457239046')
                elif response == "щи":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Chi.TXT'),
                                 attachment='photo-194978607_457239047')
                elif response == "грибной суп":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Gribnoy_soup.TXT'),
                                 attachment='photo-194978607_457239045')
                elif response == "уха":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Yuha.TXT'),
                                 attachment='photo-194978607_457239050')

                elif response == "сырный суп":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Cheeze_soup.TXT'),
                                 attachment='photo-194978607_457239049')

                elif response == "солянка":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Solyanka.TXT'),
                                 attachment='photo-194978607_457239052')
                elif response == "рассольник":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Rassolnik.TXT'),
                                 attachment='photo-194978607_457239051')
                elif response == "шурпа":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Shurpa.TXT'),
                                 attachment='photo-194978607_457239048')
                elif response == "суп с фрикадельками":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Soup_with_frikadelki.TXT'),
                                 attachment='photo-194978607_457239053')
                elif response == "куриный суп с вермишелью":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\pfirst_food\Kuriniy_soup_with_vermishel.TXT'),
                                 attachment='photo-194978607_457239054')

                    #Вторые блюда (для рандома):
                elif response == "бефстроганов":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Befstroganov.TXT'),
                                 attachment='photo-194978607_457239061')
                elif response == "голубцы":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Golubcy.TXT'),
                                 attachment='photo-194978607_457239063')
                elif response == "плов":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Plov.TXT'),
                                 attachment='photo-194978607_457239059')
                elif response == "гуляш":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Gulyash.TXT'),
                                 attachment='photo-194978607_457239056')
                elif response == "отбивная из курицы":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Otbivhie_iz_kurici.TXT'),
                                 attachment='photo-194978607_457239064')
                elif response == "паста карбонара":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Pasta_Karbonara.TXT'),
                                 attachment='photo-194978607_457239058')
                elif response == "запеканка мясная":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Zapekanka.TXT'),
                                 attachment='photo-194978607_457239057')
                elif response == "лагман":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Lagman.TXT'),
                                 attachment='photo-194978607_457239060')
                elif response == "картофель тушёный":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Kartofel_tusheniy.TXT'),
                                 attachment='photo-194978607_457239055')
                elif response == "джамбалайя":
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=openfile.open_in('recipes\second_food\Jambalaya.TXT'),
                                 attachment='photo-194978607_457239062')

                elif response == "шаурма с курицей":
                    send_message(vk_session, 'user_id', event.user_id, message=openfile.open_in('recipes/shaurma'),
                                 attachment='photo-194978607_457239033')

            elif response == "Здоровое питание":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите категорию', keyboard=keyboard)
            elif response == "Джанк фуд":
                send_message(vk_session, 'user_id', event.user_id, message='Выберите категорию', keyboard=keyboard)






