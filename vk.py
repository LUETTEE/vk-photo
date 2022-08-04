
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                     ___          ___   __   ___                                                     #
#                                                     \  \        /  /  |  | /  /                                                     #
#                                                      \  \      /  /   |  |/  /                                                      #
#                                                       \  \    /  /    |     /                                                       #
#                                                        \  \  /  /     |     \                                                       #
#                                                         \  \/  /      |  |\  \                                                      #
#                                                          \____/       |__| \__\                                                     #
#                                                                                                                                     #
#                                                            author: LUETTEE                                                          #
#                                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





# ************************************************************   LIBS   ************************************************************* #

from  os   import system
from color import *

try: import aiohttp; import asyncio
except:
    print(f'\n\n')
    print(f'{  RED  }                     ВОЗНИКЛА ОШИБКА С БИБЛИОТЕКАМИ       ')
    print(f'                                                                   ')
    print(f'{ WHITE } спиксок дополнительных библиотек:                        ')
    print(f'{PURPLE }   > {TEXT}asyncio                                        ')
    print(f'{PURPLE }   > {TEXT}aiohttp                                        ')
    print(f'                                                                   ')
    print(f'{PURPLE2} 1 {GRAY} -> {WHITE} установить библиотеки автоматически  ')
    print(f'{PURPLE2} 2 {GRAY} -> {WHITE} установить библиотеки вручную {SBROS}')

    while True:
        enter = input(f'\n{GREEN} выбери 1/2: {TEXT2}'); print(SBROS, end='')

        if enter == '1':
            try: print(f'\n{GRAY} УСТАНОВКА {PURPLE2}asyncio {SBROS}'); system('pip3 install asyncio'); import asyncio
            except: print(f'\n\n{RED} asyncio не установилась \n\n'); exit()
            
            try: print(f'\n{GRAY} УСТАНОВКА {PURPLE2}aiohttp  {SBROS}'); system('pip3 install aiohttp'); import aiohttp
            except: print(f'\n\n{RED} aiohttp не установилась \n\n'); exit()
            
            break
        elif enter == '2': exit()
        else: pass





# *********************************************************   JSON   ***************************************************************** #

# конвертирование строки в json
def json(stroka: str = '') -> dict:
    json = {}        # возвращаемый словарь
    Status = 'none'  # статус текущего символа
    key = ''         # имя текушего ключа
    meaning = ''     # значение текущего ключа
    count = 0        # номер текущего вложеного списка или словаря 
    for simvol in stroka:
        # ключ
        if Status == 'key':
            if simvol == '"': Status = ':'
            else: key += simvol

        # переход от имени ключа к значению
        elif Status == ':': Status = 'meaning'
        
        # значение ключа
        elif Status == 'meaning':
            if count == 0:
                if simvol == ',' or simvol == '}':
                    if meaning[0] == '"':
                        meaning = meaning[1:-1]
                    json[key] = meaning
                    key = ''; meaning = ''
                    Status = 'none'
                    continue
            if   simvol == '[' or simvol == '{': count += 1
            elif simvol == ']' or simvol == '}': count -= 1
            
            if simvol != r'\ '[0]: meaning += simvol

        elif Status == 'none':
            if simvol == '"': Status = 'key'

    return json





# **********************************************************   VK   ****************************************************************** #

class Vk:
    # формироваие экземпляпа класса
    def __init__(self, version: float = 5.131 ) -> None:
        self.version = version  # версия апи    

        self.loop = asyncio.get_event_loop() 

        self.ApiSession = aiohttp.ClientSession()     # ссеися для http запросов к api vk
        self.UploadSession = aiohttp.ClientSession()  # ссесия для http запросов загрузки фотографий 

    # авторизация пользователя
    def auth(self, token: str) -> None:
        self.token = token          # токен пользователя



    # (декоратор) сохраняет асинхронную main функцию 
    def MainSave(self, func) -> None:
        self.Main = func

    # запускает асинхронную main функцию
    def MainStart(self) -> None:
        try:
            self.loop.run_until_complete(self.Main())         # запуск асинхронной main функции  
        except aiohttp.client_exceptions.ClientConnectorError:
            print(f"\n{RED}  ОШИБКА {GRAY} -> {WHITE} нет подключения к интернету \n")
        finally:
            self.loop.run_until_complete(self.SessionExit())  # закрытие ссесий aiohttp

    # закрывает ссесии aiohttp
    def Exit(self) -> None:
        self.loop.run_until_complete(self.SessionExit())  # закрытие ссесий aiohttp
    


    # обращение к api vk
    async def api(self, METHOD: str, **params: dict) -> dict:
        PARAMS = '' # конвертирование всех праметров в строку для запроса
        for argument, meaning in params.items():
            if meaning == None: meaning = ''
            PARAMS += argument + '=' + str(meaning) + '&' 
        
        async with self.ApiSession.get(f"https://api.vk.com/method/{METHOD}?{PARAMS}access_token={self.token}&v={self.version}", ssl=False) as response:
            response = await response.json()

            if 'error' in response: 
                return response
                # print(f'{RED} ОШИБКА ПРИ ЗАПРОСЕ К API VK')
                # print(f'{response} {SBROS}')

            return response['response']



    # загрузка фотографий в альбом пользователя
    async def UploadPhotoAlbom(self, album_id: int, file: str) -> None:
        resp = await self.api('photos.getUploadServer', album_id=album_id)

        # если сервер вернур ошибку, допустим  > Flood Control <  :)
        if 'error' in resp:       # ОШИБКА ОТ ВК  > 9 -> Flood Control
            print(f"\n\n{RED} ОШИБКА ОТ ВК {GRAY}>{WHITE} {resp['error']['error_code']} {GRAY}->{WHITE} {resp['error']['error_msg']} \n {SBROS}")
            exit()
        
        url = resp['upload_url'] # ссылка для загрузки фотографии

        # загрузка пяти фотографий
        async with self.UploadSession.post(url, data={'file1': open(file, 'rb'), 'file2': open(file, 'rb'), 'file3': open(file, 'rb'), 'file4': open(file, 'rb'), 'file5': open(file, 'rb')}, ssl=False) as response:
            response = json(await response.text())
            
            return {'album_id':album_id, 'server':response['server'], 'photos_list':response['photos_list'], 'hash':response['hash']}



    # закрытие ссесий aiohttp
    async def SessionExit(self) -> None:
        await self.ApiSession.close()
        await self.UploadSession.close()