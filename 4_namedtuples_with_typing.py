"""
Использование typing.NamedTuple — памяти потребляем как обычный namedtuple,
но при этом можно указывать типы данных в атрибутах класса.
Лучший по эффективности способ замены Dict.
"""
from dataclasses import dataclass
import random
from typing import NamedTuple

from pympler import asizeof


def humanize_bytes(num, suffix='B'):
    """Форматирует размер в байтах в человекочитаемый вид"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class RecordNamedTuple(NamedTuple):
    shop_id: int
    delivery_days: int
    delivery_price: int

many_namedtuples2 = []
for i in range(1000):
    many_namedtuples2.append({
        'city': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
        'tariffs': [
            RecordNamedTuple(
               shop_id=random.randint(1, 10000),
               delivery_days=random.randint(1, 12),
               delivery_price=random.randint(125, 888)
            ) for _ in range(3)
        ]
    })
print(f'List[namedtuple2], размер в памяти: '
      f'{humanize_bytes(asizeof.asizeof(many_namedtuples2))}')
