from os import environ


local_link = environ.get('DEFAULT_LOCAL_PATH')  # TODO
base_notice = environ.get('BASE_URL') or 'https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?noticeId='
