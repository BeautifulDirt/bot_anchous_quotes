#!/usr/bin/env python
# --coding:utf-8--

# bySnopkovaAlla
# my profile on github: https://github.com/BeautifulDirt/

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
import random

token="1a2b3c..." # ваш токен
vk = vk_api.VkApi(token=token)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 112233) # "112233" - id вашего сообщества
upload = vk_api.VkUpload(vk)

def anchous_text(id):
    c = ['От нее толку, как от меня в хозяйстве. Она тупо гадит всем и везде',
    'Блин, тогда стоит мне задуматься. У моего брата грудь больше, чем у меня &#128579;',
    'Каждый новый человек в конфе меня пугает &#128528;',
    'Чувствую себя коллектором. Не знаю почему...',
    'Памагити плес тупому существу :с',
    'Май нейм из тупое существо',
    'Тупым существом только я могу себя называть!',
    'Тупое существо на то и тупое, что умнее не станет',
    'ПАДАЖДИТЕ! Я в одеяле запуталась... Всё, продолжайте &#128578;',
    'В том десятилетии...',
    'Преступникам похер, что Новый год',
    'Мне лечиться надо, я знаю',
    '*смонтировала видео* Как такое возможно? Узнаете, как такое возможно!',
    'А потому шо открыто всо! В твоем профиле не только на тебя компромат нароешь...',
    '*Катя нашла моменты из серий про Начальство в Зепето* Не думала, что скажу это, но аж интересно стало, какие такие моменты?',
    '*про бомбу-серию* Там может вообще - тайны исчезновения печенек из лаборатории. Вот, и всё! И тут все надумали себе: там Катюха уже Начальство 350 раз поженила, там они потрахались пару раз, да... Как бы, а на самом деле, вообще и не с ними связано!',
    'Это... это пиздец, ребята',
    '*про сериал "Эпидемия"* Какое-то заумное слово - химическое, явно! Я не знаю, я такое сразу не запоминаю, даже не воспринимаю. Шо это такое? Набор букв, какой-то... ',
    'Закрывай всю инфу, которая есть у тебя на странице! Потому что у тебя открыто просто ВСЁ! Просто читай, как открытую книгу, реально. Вот училась сначала здесь, потом там, потом тут, потом, вот, шарага. Потом вот, значит, тогда-то родилась, живу вот здесь. Давай еще, блин, станцию метро напишем и адрес, 7 этаж, квартиру - вот все такое. Комната находится вот здесь! Вот, давай, ага!',
    'Ну короче вместе ляжем &#128514;&#127770;',
    'У меня уже от всего этого... Большого количества ненужной информации просто мозг кипит, а у меня температура не спадает... Теперь понятно из за чего!',
    'Я пытаюсь сказать, но не могу сказать то, что хочу сказать, потому что я ржу &#128514;&#128514;&#128514;',
    'Не, ну, Ванга - это, знаете, сомнительное прозвище. Я могу тоже предсказать, например, то, что через 10 минут я пошлю ее нахер, и пожалуйста, это тоже сбудется!',
    'НЕСИТЕ ЧАЙ С ШИПОВНИКОМ И ТРЯПКИ, ТУТ ЩАС ПОТОП БУДЕТ',
    'Ну то, что как цитата отмечено, это ж капля в море моего долбоебизма&#128525;',
    'Катюху бояться, как срать стоя. Звучит смешно',
    'Золотых, да! Это вам не Катюхина НЦа. Сунул, плюнул и Галчонок',
    'Алла защищает диплом и стриптизершу',
    'Ну, то, что Хутепова ебанутая - это не теорема, а аксиома, ребят!',
    'ТаГ&#127770;',
    'Алло, Оль, здравствуй, вот тут такое дело: 4 придурка придут, нужно их как-то принять...',
    'Короче, девчат, я не знаю в какое дерьмо мы вляпались, но это круто!',
    'У меня все ещё ощущение, что я сплю. Слишком круто, слишком просто всё. Даже подозрительно&#128514;',
    'Ну, нихуя ж себе',
    'Пиздец селебряти, блять',
    'Ты погляди какое догадливое животное',
    'Когда Алла называет Наташу Натахой, надо, чтобы Наташа называла Аллу Аллах&#128514;. Натаха и Аллах&#128514;',
    'Ну, зачем я это напомнила сама себе? Дебила, блять, кусок',
    'Ну, и ваще и че это? Че это все спать пошли, я не понела? Так хорошо же общались, давайте еще поговорим',
    'Если Катюхи не было двое суток в ВК, значит она двое суток не спускалась в метро!',
    'Кать, я понимаю, что у тебя Начальство головного мозга, но может прекратим?',
    'Ой, как же мне хорошо! Я подарю им свои бестыжие глаза&#128514;',
    'Скажу цитатой невеликих: «Так бы сразу и сказала»']
    i = random.randint(0, len(c)-1)
    vk.method("messages.send", {"peer_id": id, "random_id": 0, "message": 'Цитата Аньчоуса: "'+c[i]+'"'})

def anchous_img(id):
    l = random.randint(1, 24)
    photo = upload.photo_messages('/img/'+str(l)+'.jpg')
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = 'photo{owner_id}_{photo_id}_{access_key}'.format(owner_id=owner_id, photo_id=photo_id, access_key=access_key)
    vk.method("messages.send", {"peer_id": id, "random_id": 0, "attachment": attachment})


while True:
    try:
        for event in longpoll.listen():
            try:
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.peer_id != event.object.from_id: # в личных сообщениях
                        pass
                    elif event.object.peer_id == event.object.from_id: # в беседе
                        msg = event.object.message['text'].lower()
                        if msg == "цитата аньчоуса":
                            j = random.randint(0, 1) # картинка или текст? вот в чем вопрос!
                            if j == 1:
                                anchous_text(event.object.message['peer_id'])
                            else:
                                anchous_img(event.object.message['peer_id'])
            except vk_api.exceptions.ApiError:
                print("Написало сообщение сообщество!") # исключение, если в беседе имеется другой бот
    except Exception as E:
        print(E)
        time.sleep(3)
