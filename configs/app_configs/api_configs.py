from os import environ

api_links = {'PARSER_URL_XML': environ.get('API_PARSER_XML_URL'),
             'PARSER_LOCAL_XML_NAME': environ.get('API_PARSER_LOCAL_XML_NAME')}

api_additional_info = {'PREFIX_URL_XML': environ.get('PREFIX_URL_XML')}
