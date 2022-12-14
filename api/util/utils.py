"""
utils.py
- providing general tools and functions

Created by Xiong Kaijie on 2022-08-13.
Contributed by: Xiong Kaijie
Copyright © 2022 team Root of ByteDance Youth Camp. All rights reserved.
"""

import time
from datetime import datetime, timedelta
from flask import jsonify


def convert_utc_to_local(utc_datetime):
    """Convert UTC timestamp to local time
    """
    if utc_datetime:
        now_timestamp = time.time()
        offset = datetime.fromtimestamp(
            now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        local_time = utc_datetime + offset
        return local_time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None


def successResponseWrap(data):
    return jsonify({
        'data': data,
        'status': 'ok',
        'msg': '请求成功',
        'code': 20000,
    })


def failResponseWrap(msg, data=None, code=50000):
    return jsonify({
        'data': data,
        'status': 'fail',
        'msg': msg,
        'code': code,
    })


def get_past_days(days, now=datetime.now()):
    return [
        (
            datetime(year=now.year, month=now.month, day=now.day) -
            timedelta(days=i)
        ).strftime('%Y-%m-%d')
        for i in range(days, 0, -1)
    ]
