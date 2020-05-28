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
        api_name = 'xml_url'
        base_name = 'base_url'
        xml_id = Auction.query.filter_by(purchase_number=number).first().notice_id
        api_parserlink = ConfigDealer.get_api_links(api_name)
        base = ConfigDealer.get_additional_info(base_name)
        xml_url = base + xml_id

        response = requests.get(api_parserlink, {'link': xml_url})
        if response.status_code == 200:
            data = response.json()['data']
            return jsonify({'status': True,
                            'data': data})

        return jsonify({'status': False,
                        'error': {'code': response.status_code,
                                  'title': response.status_code,
                                  'detail': 'ERROR'}})

    return jsonify({'status': False,
                    'error': {'message': 'Номер аукиона не получен'}})


@api.route('/notice')
def save_notice():
    """Записать информацию в БД"""
    local_path = request.args.get('local_path') or ConfigDealer.get_additional_info('local_path')
    if local_path:
        api_name = 'xml_id'
        api_parserlink = ConfigDealer.get_api_links(api_name)

        response = requests.get(api_parserlink, {'link': local_path})
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

    return jsonify({'status': False,
                    'error': {'message': 'Ссылка на локальные файлы не получена <local_path>'}})
