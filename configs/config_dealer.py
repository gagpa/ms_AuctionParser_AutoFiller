from configs.app_configs import main_configs, api_additional_info, api_links


class ConfigDealer:
    __main = main_configs
    __api_links = api_links
    __api_additional_info = api_additional_info

    @classmethod
    def get_main_config(cls, config_name):
        """Получить основной конфиг для инициализации приложения(app)"""
        try:
            config = cls.__main[config_name]
            return config()
        except KeyError:
            print(f'Ваш ключ: {config_name} не подходит. Возможные ключи: {cls.__main.keys()}')
            raise KeyError

    @classmethod
    def get_api_links(cls, api_name):
        """Получить Api-ссылки"""
        try:
            config = cls.__api_links[api_name]
            return config
        except KeyError:
            print(f'Ваш ключ: {api_name} не подходит. Возможные ключи: {cls.__api_links.keys()}')
            raise KeyError

    @classmethod
    def get_api_additional_info(cls, info_name):
        """Получить дополнительную информацию"""
        try:
            config = cls.__api_additional_info[info_name]
            return config
        except KeyError:
            print(f'Ваш ключ: {info_name} не подходит. Возможные ключи: {cls.__api_additional_info.keys()}')
            raise KeyError
