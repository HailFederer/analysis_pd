import sys
from urllib.request import Request, urlopen
from datetime import *
import json


# def json_error(e):
#     print("%s : %s" % (e, datetime.now()), file=sys.stderr)


# def json_request(url='', encoding='utf-8', success=None, error=json_error):
def json_request(url='', encoding='utf-8', success=None, error=lambda e: print("%s : %s" % (e, datetime.now()), file=sys.stderr)):
    try:
        resp = urlopen(Request(url))
        resp_body = resp.read().decode(encoding)
        json_result = json.loads(resp_body)

        print('%s : success for request [%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

    except Exception as e:
        callable(error) and error(e)
        # print("%s : %s" % (e, datetime.now()), file=sys.stderr)
