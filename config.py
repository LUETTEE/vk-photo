import json


# работа с config
def Config(config: dict | None = None) -> dict | None:
    # возвращает словарь из конфига
    if config == None:
        with open("config.json", "r") as file:
            return json.load(file)
    
    # записывает словарь в конфиг
    else:
        with open("config.json", "w") as file:
            json.dump( config, file )





# работа с token в конфиге
def Token(token: str = 'none') -> str | None:
    # возвращает токен из конфига
    if token == 'none':
        return Config()['token']

    # записывает токен в конфиг
    else:
        config = Config()
        config['token'] = token
        Config(config)





# работа с clear в конфиге
def Clear(clear: str = 'none') -> str | None:
    # возвращает clear из конфига
    if clear == 'none':
        return Config()['clear']

    # записывает clear в конфиг
    else:
        config = Config()
        config['clear'] = clear 
        Config(config)
