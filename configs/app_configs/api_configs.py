from os import environ

api_links = {'xml_url': environ.get('API_XML_URL'),
             'xml_id': environ.get('API_XML_ID')}

additional_info = {'prefix_url': environ.get('PREFIX_URL'),
                   'local_path': environ.get('DEFAULT_LOCAL_PATH')}
