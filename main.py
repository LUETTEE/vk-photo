
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                                                     #
#                $$$$         $$$$       $$$$ $$$$$$$$$$$$ $$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$ $$$$$$$$$$$$ $$$$$$$$$$$$                #
#                $$$$         $$$$       $$$$ $$$$$$$$$$$$ $$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$ $$$$$$$$$$$$ $$$$$$$$$$$$                #
#                $$$$         $$$$       $$$$ $$$$               $$$$             $$$$       $$$$         $$$$                        #
#                $$$$         $$$$       $$$$ $$$$$$$$$$$$       $$$$             $$$$       $$$$$$$$$$$$ $$$$$$$$$$$$                #
#                $$$$         $$$$       $$$$ $$$$$$$$$$$$       $$$$             $$$$       $$$$$$$$$$$$ $$$$$$$$$$$$                #
#                $$$$         $$$$       $$$$ $$$$               $$$$             $$$$       $$$$         $$$$                        #
#                $$$$$$$$$$$$   $$$$   $$$$   $$$$$$$$$$$$       $$$$             $$$$       $$$$$$$$$$$$ $$$$$$$$$$$$                #
#                $$$$$$$$$$$$    $$$$$$$$$    $$$$$$$$$$$$       $$$$             $$$$       $$$$$$$$$$$$ $$$$$$$$$$$$                #
#                                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





# ************************************************************   LIBS   ************************************************************* #

from   os   import system  # вводит текст как команду в терминал
from  time  import sleep   # стопит код на n секунд 
from   vk   import Vk      # клаас для работы с api vk
from config import *       # управление конфигом
from color  import *       # палитра нужных цветов





# ************************************************************   BANNER   *********************************************************** #


def banner() -> None:
    system(CLEAR)                                                                                     # *очищает терминал*
    print(f"{ BLUE }       _     { PURPLE }   { GRAY }                      { SBROS }"); sleep(0.02)  #        _                             
    print(f"{ BLUE }      | | __ { PURPLE } P { GRAY }                      { SBROS }"); sleep(0.02)  #       | | __  P                      
    print(f"{ BLUE } __   |__/ / { PURPLE } H { GRAY }    # # # # # # # # # { SBROS }"); sleep(0.02)  #  __   |__/ /  H     # # # # # # # # #
    print(f"{ BLUE } \ \  / / /  { PURPLE } O { GRAY }    > L U E T T E E < { SBROS }"); sleep(0.02)  #  \ \  / / /   O     > L U E T T E E <
    print(f"{ BLUE }  \ \/ /  \  { PURPLE } T { GRAY }    # # # # # # # # # { SBROS }"); sleep(0.02)  #   \ \/ /  \   T     # # # # # # # # # 
    print(f"{ BLUE }   \__/_|\_\ { PURPLE } O { GRAY }                      { SBROS }"); sleep(0.02)  #    \__/_|\_\  O                      





# ************************************************************   TOKEN   ************************************************************ #

# функция смены токена
def TOKEN() -> None :
    print('\n' + f"{TEXT}  получить {RED}access token                    "); sleep(0.02) #  получить access token
    print(       f"{TEXT}  можно по ссылке {RED}https://vkhost.github.io "); sleep(0.02) #  можно по ссылке https://vkhost.github.io

    enter = input(f"\n{GREEN} token {GRAY}-> {TEXT2}"); print(SBROS, end='') # ввод токена

    if enter == '0': pass  # отменить замену токена
    else: Token(enter)     # заменить токен





# *************************************************************   MAIN   ************************************************************ #

vk = Vk()
@vk.MainSave
async def main() -> None:

    # $$$$$$$$$$$$$$$$$$$$$$$$$ проверка токена $$$$$$$$$$$$$$$$$$$$$$$$$ #

    # бесконечный цикл, пока токен не станет правельным 
    while True:  
        vk.auth(Token())                              # авторизация пользователя
        prof = await vk.api('account.getProfileInfo') # тестовый запрос к апи
        # если токен не верный
        if 'error' in prof: 
            print(f'\n {RED} ОШИБКА {GRAY} -> {WHITE} установлен неправильный токен')
            TOKEN()  # функция смены токена
            banner() # ввывод баннера
        # если токен верный
        else: break



    # $$$$$$$$$$$$$$$$$$$$$$$$$ выбор альбома $$$$$$$$$$$$$$$$$$$$$$$$$ #

    print(f"\n {GRAY}    в какой альбом загружать фотки? \n")
    print(f" {PURPLE2} 1 {GRAY} -> {TEXT} создать новый альбом                "); sleep(0.02)
    print(f" {PURPLE2} 2 {GRAY} -> {TEXT} использовать уже существующий альбом"); sleep(0.02)

    while True: # бесконечный цикл, пока enter не будет соответствовать нужным параметрам
        enter = input(f'\n{GREEN} выбери 1/2: {TEXT2}'); print(SBROS, end='')

        # новый альбом
        if enter == '1':
            title = input(f'\n{GREEN} название для нового альбома: {TEXT2}')
            album = await vk.api('photos.createAlbum', title=title) # создание нового альбома
            album_id = album['id']
            break

        # существующий альбом
        elif enter == '2': 
            albums = await vk.api('photos.getAlbums') # получение всех альбомов пользователя
            albums = albums['items']
            albomes = [] # список для удобной работы со списком альбомов

            # заполнение albomes только нужными данными
            for i in range(len(albums)): albomes.append({ 'rowid': i + 1, 'id': albums[i]['id'], 'title': albums[i]['title'] })

            # вывод списка альбомов пользователя
            print(f'\n {GRAY}        альбомы   \n'); sleep(0.02)
            for album in albomes: print(f"{PURPLE} {album['rowid']} {GRAY} -> {WHITE} {album['title']} "); sleep(0.02)

            # выбор альбома из списка выведенного ранее
            cycle = True
            while cycle: # бесконечный цикл, пока enter не будет соответствовать нужным параметрам
                enter = input(f"\n{GREEN} номер альбома: {TEXT2}"); print(SBROS, end='')
                
                for album in albomes:
                    if str(album['rowid']) == enter:
                        album_id = album['id']
                        cycle = False
            break

        elif enter == '0': exit()
        else: pass

    

    # $$$$$$$$$$$$$$$$$$$$$$$$$ выбор фотки $$$$$$$$$$$$$$$$$$$$$$$$$ #

    while True: # бесконечный цикл, пока enter не будет соответствовать нужным параметрам
        file = input(f"\n{GREEN} расположение фотки > {TEXT2}"); print(SBROS, end='')
        try:
            f = open(file, 'rb') # открывет файл по указанному пути
            f.close()            # закрывает файл
            break
        except: pass
    


    # $$$$$$$$$$$$$$$$$$$$$$$$$ количество фоток $$$$$$$$$$$$$$$$$$$$$$$$$ #

    print(f"\n {GRAY} количество фоток должно быть кратно пяти")
    while True: # бесконечный цикл, пока enter не будет соответствовать нужным параметрам
        count = input(f"\n{GREEN} количество фоток > {TEXT2}"); print(SBROS, end='')
        try:
            count = int(count)
            if count % 5 == 0: break
        except: pass



    # $$$$$$$$$$$$$$$$$$$$$$$$$ загрузка фотографий $$$$$$$$$$$$$$$$$$$$$$$$$ #

    print(f"\n {WHITE} загружено {GRAY} -> {PURPLE} 0", end='')

    resp = await vk.UploadPhotoAlbom(album_id=album_id, file=file) # загружает 5 копий одной фотографии
    
    album_id    = resp['album_id']
    server      = resp['server']
    photos_list = resp['photos_list']
    hash        = resp['hash']

    count = (count // 5) + 1
    for i in range(1, count):
        # дублирует фотки в альбом по 5 штук за раз 
        resp = await vk.api('photos.save', album_id=album_id, server=server, photos_list=photos_list, hash=hash)
        
        # если сервер вернур ошибку, допустим  > Flood Control <  :)
        if 'error' in resp:       # ОШИБКА ОТ ВК  > 9 -> Flood Control
            print(f"\n\n{RED} ОШИБКА ОТ ВК {GRAY}>{WHITE} {resp['error']['error_code']} {GRAY}->{WHITE} {resp['error']['error_msg']} \n {SBROS}")
            exit()
        else:
            id = i * 5
            print(f'\r {WHITE} загружено {GRAY} -> {PURPLE} {id}', end='')

    print('\n')





# ************************************************************   MENU   ************************************************************* #

def menu() -> None:
    print(f"                                            {SBROS}"); sleep(0.02)   # 
    print(f" {PURPLE2} 1 {GRAY} -> {TEXT} запустить     {SBROS}"); sleep(0.02)   #  1  ->  запустить
    print(f" {PURPLE2} 2 {GRAY} -> {TEXT} сменить токен {SBROS}"); sleep(0.02)   #  2  ->  сменить токен
    
    while True: # бесконечный цикл, пока enter не будет соответствовать нужным параметрам
        enter = input(f'\n{GREEN} выбери 1/2: {TEXT2}'); print(SBROS, end='')

        if   enter == '1': banner(); vk.MainStart(); break
        elif enter == '2': banner(); TOKEN(); banner(); menu(); break
        elif enter == '0': exit()
        else: pass





# ************************************************************   START   ************************************************************ #

try:
    CLEAR = Clear()
    if CLEAR == 'none':
        print(f'\n\n')
        print(f'{  RED  }                ВВЕДИТЕ КОМАНДУ ОЧИСТКИ ТЕРМИНАЛА            ')
        print(f'                                                                      ')
        print(f'{ WHITE } комады очистки на популярных OC:                            ')
        print(f'{PURPLE }  {TEXT} clear {GRAY} -> {WHITE} linux, mac, android, termux ')
        print(f'{PURPLE }  {TEXT} cls {GRAY} -> {WHITE} windows                       ')
        
        Clear(input(f'\n{GREEN} комады очистки > {TEXT2}')); print(SBROS, end='')
        CLEAR = Clear()

    banner()
    menu()

except KeyboardInterrupt:
    vk.Exit()
    print(f'\n\n{RED}   ВЫХОД \n {SBROS}')