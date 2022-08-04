# LUETTEE -> VK - PHOTO < #




## СОДЕРЖАНИЕ ##

- [ИНФО](#info)
  - [для чего этот код](#meaning)
  - [максимальное количество фоток](#MaxCount)
  - [сколько загружать фотографий](#count)
  - [могут ли забанить](#ban)
  - [почему код такой всратый](#govnocode)
- [установка и запуск](#install)
- [алгоритм кода](#algoritm)
- [связь со мной](#connection)




<a name="info"/>

## ИНФО ##

<a name="meaning"/>

- ### для чего этот код ###
  Код загружает одну и туже картинку в альбом несколько раз
  
<a name="MaxCount"/>

- ### максимальное количество фоток ###
  Максимальное количество фотографий в одном альбоме, 10 000. Это ограничение самого ВК, а не кода
  
<a name="count"/>

- ### сколько загружать фотографий ###
  Желательно в день грузить 5 000 - 7 000 фоток, иначе вк может вам запретить загружать фотки на целые сутки,
  вы не сможете загружать фотографии даже в личных сообщениях
  
<a name="ban"/>

- ### могут ли забанить ###
  Я грузил много фоток (исключительно для тестов), и меня не банили. Был только запрет на загрузку фотографий (Flood Control). Но если вас забанят, то я не виноват)
  
<a name="govnocode"/>

- ### почему код такой всратый ###
  потому что автор кода [LUETTEE](https://github.com/LUETTEE)
  
  
  
  
<a name="install"/>

## установка и запуск ##

-     git clone https://github.com/LUETTEE/vk-photo
-     cd vk-photo
-     python3 main.py




<a name="algoritm"/>

## алгоритм кода ##

- загрузка 5 экземпляров выбранной фотки
- получение данных этих фотографий для сохранения их в альбом
- дублируется сохранение фотографий в альбом N раз

Возникает вопрос

     Если фотки дублируются, а не грузятся, почему тогда код такой медленный?

Потому что данные фотографий (photo_list) очень длинные и запрос получается большим.

Всё же я бы не сказал, что код медленный. Потому что раньше я использовал requests для http запросов. 
А это синхронная библиотека, которая работает раза в 2 медленее. Да и кто му же раньше, я загружал каждую фотку по отдельности.
Сейчас же я использую асинхронный код, сохраняю за один запрос 5 фоток и дублирую фотки, а не заново загружаю их.
Поэтому для меня код работает очень даже быстро)




<a name="connection"/>

## связь со мной ##

Если есть идеи или вы хотели бы мне рассказать, что я делаю не так, вы всегда можете связать со мной в вк [@luettee](https://vk.com/luettee)



----

###### Я написал этот код, просто от скуки, а не для того чтобы вы засоряли сервера нашего любимого ВК ######
