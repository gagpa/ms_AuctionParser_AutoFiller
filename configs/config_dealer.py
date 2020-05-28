from configs.app_configs import main_configs, additional_info, api_links


class ConfigDealer:
    __main = main_configs
    __api_links = api_links
    __additional_info = additional_info

    @classmethod
    def get_main(cls, config_name):
        try:
            config = cls.__main[config_name]
            return config()
        except KeyError:
            print(f'Ваш ключ: {config_name} не подходит. Возможные ключи: {cls.__main.keys()}')
            raise KeyError

    @classmethod
    def get_api_links(cls, api_name):
        try:
            config = cls.__api_links[api_name]
            return config
        except KeyError:
            print(f'Ваш ключ: {api_name} не подходит. Возможные ключи: {cls.__api_links.keys()}')
            raise KeyError

    @classmethod
    def get_additional_info(cls, info_name):
        try:
            config = cls.__additional_info[info_name]
            return config
        except KeyError:
            print(f'Ваш ключ: {info_name} не подходит. Возможные ключи: {cls.__additional_info.keys()}')
            raise KeyError
