import decimal
import logging
import uuid
from datetime import date, datetime
from typing import (
    Callable, Collection, Dict, List, Optional, Set, Tuple, Union
)
from urllib.parse import urlparse

import orjson
from loguru import logger
from pydantic import UUID4, BaseModel
from pydantic.fields import ModelField

from project.settings.configs import APPLICATION


def today():
    """
    get today
    :return: date
    """
    return date.today()


def get_current_date():
    return datetime.now()


def fields_required(fields: Union[Dict, List, Set, str, int], data_check: Union[Dict, List]) -> (bool, List):
    _data_check = []
    if isinstance(data_check, Dict):
        _data_check.append(data_check)
    elif isinstance(data_check, List):
        _data_check = [*_data_check, *data_check]

    _fields = set()
    if isinstance(fields, (List, Tuple, Set)):
        _fields = {*list(data_check)}
    elif isinstance(fields, (str, int)):
        _fields.add(fields)

    miss_key = set()

    for temp in _data_check:
        if isinstance(data_check, Dict):
            _key = set(temp.keys()) - _fields
            if _key:
                miss_key = {*miss_key, *_key}
        else:
            miss_key = _fields
            break
    if miss_key:
        return False, miss_key
    return True, None


def generate_uuid() -> str:
    """
    :return: str
    """
    return str(uuid.uuid4())


def travel_dict(d: dict, process_func: Callable):
    process_func(d)
    if isinstance(d, Dict):
        for key, value in d.items():
            if type(value) is dict:
                travel_dict(value, process_func)
            elif isinstance(value, (list, set, tuple,)):
                for item in value:
                    travel_dict(item, process_func)
            else:
                process_func((key, value))
    return d


def travel_dict_v2(d: dict, process_funcs: List[Callable]):
    for func in process_funcs:
        func(d)
    if isinstance(d, Dict):
        for key, value in d.items():
            if type(value) is dict:
                travel_dict_v2(value, process_funcs)
            elif isinstance(value, (list, set, tuple,)):
                for item in value:
                    travel_dict_v2(item, process_funcs)
            else:
                for func in process_funcs:
                    func((key, value))
    return d


def process_generate_uuid(d):
    if isinstance(d, dict) and ("uuid" in d) and (d["uuid"] is None):
        d.update({"uuid": generate_uuid()})


def process_find_uuid_delete(d, uuid):
    if isinstance(d, dict) and ("uuid" in d) and str(d["uuid"]) == uuid:
        d.clear()


def process_generate_uuid4(d):
    if isinstance(d, dict) and ("uuid" in d) and (d["uuid"] is None):
        d.update({"uuid": uuid.uuid4()})


def convert_to_num(n):
    if not n:
        return None
    try:
        n = float(n)
    except ValueError:
        return None
    if float(n).is_integer():
        return int(n)
    return float(n)


def is_integer_num(n):
    if not n:
        return None
    try:
        float(n)
    except ValueError:
        return 0
    if float(n).is_integer():
        return int(n)
    return float(n)


def los_round(num, d_places):
    rs = float(decimal.Decimal(str(num)).quantize(decimal.Decimal('0.' + ('0' * d_places)), rounding=decimal.ROUND_HALF_UP))
    return rs


def los_round_down(num, d_places):
    rs = float(decimal.Decimal(str(num)).quantize(decimal.Decimal('0.' + ('0' * d_places)), rounding=decimal.ROUND_DOWN))
    return rs


def to_lower_dash(s: str):
    return s.lower().replace("_", "-")


def to_pascal_case(s: str):
    return "".join([part[0:1].upper() + part[1:] for part in s.split("_")])


def insert_body(e):
    loc = list(e["loc"])
    loc.insert(0, "body")
    e["loc"] = tuple(loc)
    return e


def insert_pre_loc(e: Dict, loc: Collection = ("body",)) -> Dict:
    e["loc"] = (*loc, *e["loc"],)
    return e


def insert_pre_locs(errors: List[Dict], pre_loc=("body",)) -> List[Dict]:
    for e in errors:
        insert_pre_loc(e, pre_loc)
    return errors


def travel_schema(schema: BaseModel, process_funcs: List[Callable]):
    for func in process_funcs:
        func(schema)
    for key in schema.__fields_set__:
        if isinstance(schema.__getattribute__(key), BaseModel):
            # If value is dict then iterate over all its values
            travel_schema(schema.__getattribute__(key), process_funcs)
        elif isinstance(schema.__getattribute__(key), List):
            # If value is not dict type then yield the value
            for item in schema.__getattribute__(key):
                travel_schema(item, process_funcs)


def handle_generate_uuid4(object_, erase_old_value: bool = False) -> None:
    if isinstance(object_, BaseModel):
        for name, info in object_.__fields__.items():
            value = object_.__getattribute__(name)
            info: ModelField
            if info.field_info.extra.get("gen_uuid") and (erase_old_value or value is None) and info.type_ == UUID4:
                object_.__setattr__(name, uuid.uuid4())


def emp_str(v) -> str:
    return str(v) if v is not None else ""


def str_to_bool(s: str) -> bool:
    return orjson.loads(s.lower())


def bool_to_str(s: bool) -> str:
    return str(s)


def append_cdn(url) -> Optional[str]:
    if url is None:
        return None
    return f"/cdn{urlparse(url)._replace(netloc='', scheme='').geturl()}"


def op(file, mode='r', encoding="utf8"):
    return open(file, mode, encoding=encoding)


def datetime_to_string(_time: datetime, _format=APPLICATION.DATETIME_INPUT_OUTPUT_FORMAT) -> str:
    if _time:
        return _time.strftime(_format)
    return ''


def string_to_datetime(string: str, default=None, _format=APPLICATION.DATETIME_INPUT_OUTPUT_FORMAT) -> datetime:
    try:
        return datetime.strptime(string, _format)
    except (ValueError, TypeError):
        return default


def date_to_string(_date: date, default='', _format=APPLICATION.DATE_INPUT_OUTPUT_FORMAT) -> str:
    if _date:
        return _date.strftime(_format)
    return default


def string_to_date(string: str, default=None, _format=APPLICATION.DATE_INPUT_OUTPUT_FORMAT) -> datetime:
    try:
        return datetime.strptime(string, _format)
    except (ValueError, TypeError):
        return default


def date_to_datetime(date_input: date, default=None) -> datetime:
    try:
        return datetime.combine(date_input, datetime.min.time())
    except (ValueError, TypeError):
        return default


def datetime_to_date(datetime_input: datetime, default=None) -> date:
    try:
        return datetime_input.date()
    except (ValueError, TypeError):
        return default


def end_time_of_day(datetime_input: datetime, default=None) -> datetime:
    try:
        return datetime_input.replace(hour=23, minute=59, second=59)
    except (ValueError, TypeError):
        return default


def date_string_to_other_date_string_format(
        date_input: str,
        from_format: str,
        to_format: str = APPLICATION.DATE_INPUT_OUTPUT_FORMAT,
        default=None
) -> Optional[str]:
    _date = string_to_date(date_input, _format=from_format)
    if not _date:
        return default

    return date_to_string(_date, _format=to_format, default=default)


def combine_full_address(number_and_street: str = None, ward: str = None, district: str = None, province: str = None) -> str:
    return ", ".join(filter(lambda x: x, (number_and_street, ward, district, province)))


def template_field_pipeline(v) -> str:
    if v is not None and type(v) == decimal.Decimal:
        v = convert_number_thousands_separator(v)
    v = emp_str(v)
    return v


def convert_number_thousands_separator(v) -> str:
    return '{0:,.0f}'.format(v).replace(",", ".")


def json_dumps(obj: Dict) -> bytes:
    def default(value):
        if isinstance(value, decimal.Decimal):
            return str(value)
        raise TypeError

    return orjson.dumps(obj, default=default)


def debug(msg):
    if logging.getLogger().level == logging.DEBUG:
        return logger.debug(msg)
