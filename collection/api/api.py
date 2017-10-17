from urllib.parse import urlencode
from datetime import datetime

import sys

import math

from .json_request import json_request

SERVICE_KEY = 'oABBCg5E85HSqBojoH367udLslxF44fPv417DVIJvL1MWs1sh7b1xM3RpmQfD6et6jhK%2Fi%2BRADCWmzhFHU2dyg%3D%3D'


def pd_gen_url(endpoint, **params):
    return '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), SERVICE_KEY)


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0
        ):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    pageNo = 1
    hasnext = True

    while hasnext:
        url = pd_gen_url(
            endpoint,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            numOfRows=100,
            _type='json',
            pageNo=pageNo
        )
        json_result = json_request(url=url)

        if json_result is None:
            break

        json_response = json_result.get('response')
        json_header = json_response.get('header')
        result_message = json_header.get('resultMsg')

        if 'OK' != result_message:
            print('%s : Error[%s] for Request(%s)' & (datetime.now(), result_message, url), file=sys.stderr)
            break

        json_body = json_response.get('body')

        numOfRows = json_body.get('numOfRows')
        totalCount = json_body.get('totalCount')

        if totalCount == 0:
            break

        last_pageNo = math.ceil(totalCount / numOfRows)
        if pageNo == last_pageNo:
            hasnext = False
        else:
            pageNo += 1

        json_items = json_body.get('items')
        yield json_items.get('item') if isinstance(json_items, dict) else None