import vk_api
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType
TOKEN ="vk1.a.yRvsrpvrGzikqHI_TBbje26JFjE6_p0XwTE5uDYxIuLgBmpLJUTOpFF9xKq-FtJ18On-X2tlTtVCbc1Fp0o6jANrNeK-pTDBxlGTlca2zAcnbVboZjW6_uIOz47yKiPOH6DIxZrm-Q_tsCs2RwGLfsbhNiXeqddxAUmzi1XojSmPIuP0XMWgDY8C8NzGkOwN3wTx1sIRSt_6AESzYCjCgA"
vk_session = vk_api.VkApi(token=TOKEN)
longpool= VkLongPoll(vk_session)
vk = vk_session.get_api()
vars = ["камень", "ножницы", "бумага"]
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me and event.text.lower() in vars:
       bot = choice(vars)
       if event.from_user:
            vk.messages.send(user_id=event.user_id, message=bot, random_id=randrange(1,100000))
            if bot == "ножницы" :
                if event.text.lower() == "ножницы":
                    user = "ничья"
                elif event.text.lower() == "камень":
                    user = "ты победил"
                else :
                    user = "ты проиграл"
            elif bot == "бумага":
                if event.text.lower() == "ножницы":
                    user = "ты победил"
                elif event.text.lower() == "камень":
                    user = "ты проиграл"
                else:
                    user = "ничья"
            else:
                if event.text.lower() == "ножницы":
                    user = "ты проиграл"
                elif event.text.lower() == "камень":
                    user = "ничья"
                else :
                    user = "ты победил"
            vk.messages.send(user_id=event.user_id,message=user, random_id=randrange(1,100000))
    else:
        if event.type ==  VkEventType.MESSAGE_NEW :
            vk.messages.send(user_id=event.user_id, message="ERROR", random_id=randrange(1,100000))
        elif event.type == VkEventType.MESSAGE_NEW:
            vk.messages.send(user_id=event.user_id, message="ERROR", random_id=randrange(1, 100000))