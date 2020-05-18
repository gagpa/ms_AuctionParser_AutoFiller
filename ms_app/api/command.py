from . import api
from ms_app import db
from ms_app.models import Auction
from ms_app.configs.api_config import api_links
from ms_app.configs.links import local_link as parse_link
from ms_app.configs.links import base_notice


import requests
from flask import jsonify, request


@api.route('/auction/<number>')
def get_auction_test(number):
    # number = request.args.get('number')
    notice_auction = Auction.query.filter_by(purchase_number=number).first()
    link = api_links['xml_url']
    xml_url = base_notice + notice_auction.notice_id
    response = requests.get(link, {'link': xml_url})
    print(xml_url)
    print(link)
    if response.status_code == 200:
        data = response.json()['data']
        return jsonify({'status': True,
                        'data': data
                        })
    return jsonify({'status': False,
                    'error': {
                        'code': response.status_code,
                        'title': response.status_code,
                        'detail': 'ERROR'
                    }
                    })


@api.route('/notice')
def save_notice():
    local_link = request.args.get('local_link', parse_link)
    if local_link:
        link = api_links['xml_id']
        response = requests.get(link, {'link': local_link})
        status = response.status_code == 200
        if status:
            for info in response.json()['data']:
                a = Auction()
                a.purchase_number = info.get('purchaseNumber')
                a.notice_id = info.get('noticeId')
                a.type_name = info.get('typeName')
                db.session.add(a)
            count = len(response.json()['data'])
            db.session.commit()
            return jsonify({'status': status,
                            'report': f'saved {count} ids'})
