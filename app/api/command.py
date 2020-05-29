import requests
from flask import jsonify, request

from app import db
from app.models import Auction
from configs import ConfigDealer
from . import api


@api.route('/auction')
def get_auction_test():
    """Получить информацию об аукционе по его номеру"""
    number = request.args.get('number')
    if number:
        notice_auction = Auction.query.filter_by(purchase_number=number).first()
        if notice_auction:
            api_name = 'PARSER_URL_XML'
            prefix_url_name = 'PREFIX_URL_XML'

            api_parserlink = ConfigDealer.get_api_links(api_name)
            prefix_url = ConfigDealer.get_api_additional_info(prefix_url_name)
            xml_id = notice_auction.notice_id
            xml_url = prefix_url + xml_id
            try:
                response = requests.get(api_parserlink, {'xml_url': xml_url})
                if response.status_code == 200:
                    data = response.json()['data']
                    return jsonify({'status': True,
                                    'data': data})

                return jsonify({'status': False,
                                'error': {'code': response.status_code,
                                          'title': response.status_code,
                                          'detail': f'Не получилось получить данные от МС {api_parserlink}'}})

            except requests.exceptions.ConnectionError:
                return jsonify({'status': False,
                                'error': {'message': 'Сервис временно не доступен'}})

        return jsonify({'status': False,
                        'error': {'message': f'Аукциона с номером {number} нет в БД'}})

    return jsonify({'status': False,
                    'error': {'message': 'Номер аукиона не получен'}})


@api.route('/notice')
def save_notice():
    """Записать информацию в БД"""
    local_path = request.args.get('local_path')
    count_files = request.args.get('count_files')

    if local_path:
        api_name = 'PARSER_LOCAL_XML_NAME'

        api_parser_link = ConfigDealer.get_api_links(api_name)
        try:
            response = requests.get(api_parser_link, {'local_path': local_path})
            if response.status_code == 200:
                data = response.json()['data']
                for auction_info in data:
                    auction_model = Auction()
                    auction_model.purchase_number = auction_info.get('purchaseNumber')
                    auction_model.notice_id = auction_info.get('noticeId')
                    auction_model.type_name = auction_info.get('typeName')
                    db.session.add(auction_model)
                count = len(data)
                db.session.commit()
                return jsonify({'status': True,
                                'report': f'saved {count} auctions ID'})

            return jsonify({'status': False,
                            'error': {'code': response.status_code,
                                      'title': response.status_code,
                                      'detail': 'ERROR'}})

        except requests.exceptions.ConnectionError:
            return jsonify({'status': False,
                            'error': {'message': 'Сервис временно не доступен'}})

    return jsonify({'status': False,
                    'error': {'message': 'Ссылка на локальные файлы не получена <local_path>'}})
