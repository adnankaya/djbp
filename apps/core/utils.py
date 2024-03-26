from django.conf import settings
from django.db import connection, reset_queries
from django.contrib.sites.shortcuts import get_current_site
import functools
import time
from django.utils import timezone
from django.utils import dateparse
import datetime


def get_domain(request):
    site = get_current_site(request)
    if settings.DEBUG:
        return f"http://{site.domain}"
    else:
        return f"https://{site.domain}"
    

def human_format(num:int):
    """
    >>> human_format(999999)
    '1M'
    >>> human_format(999499)
    '999K'
    >>> human_format(9994)
    '9.99K'
    >>> human_format(9900)
    '9.9K'
    >>> human_format(6543165413)
    '6.54B'

    src: https://stackoverflow.com/a/45846841/5491260
    """
    if not isinstance(num, int):
        return None
    num = float("{:.3g}".format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return "{}{}".format(
        "{:f}".format(num).rstrip("0").rstrip("."), ["", "K", "M", "B", "T"][magnitude]
    )


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_today_with_timezone():
    today = timezone.make_aware(
        timezone.datetime.today(), timezone.get_default_timezone()
    )
    return today


def convert_unix_to_datetime(unix_time: int):
    if not isinstance(unix_time, int):
        raise ValueError(f"convert_unix_to_datetime::Expected unix_time as integer!")
    if unix_time % 1000 == 0:
        unix_time = unix_time / 1000.0
    return datetime.datetime.utcfromtimestamp(unix_time)


def convert_iso_to_datetime(timestamp: str):
    """
    in => "2023-08-11T11:28:45+0000"
    out => datetime.datetime(2023, 8, 11, 11, 28, 45, tzinfo=datetime.timezone.utc)
    """
    return dateparse.parse_datetime(timestamp)


def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        # print("_"*100)
        # print(connection.queries)
        # print("_"*100)

        end_queries = len(connection.queries)
        print("=" * 100)
        print(f"Function : {func.__qualname__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.4f}s")
        print("=" * 100)
        return result

    return inner_func
