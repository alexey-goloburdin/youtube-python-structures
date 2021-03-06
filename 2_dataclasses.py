"""
Использование dataclass позволяет снизить объём затрачиваемой оперативной
памяти, а также за счёт указания типов данных в атрибутах класса улучшает
читаемость кода и облегчает разработку в IDE.
"""
from dataclasses import dataclass
import random

from pympler import asizeof


def humanize_bytes(num, suffix='B'):
    """Форматирует размер в байтах в человекочитаемый вид"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


@dataclass
class RecordDataClass:
    shop_id: int
    delivery_days: int
    delivery_price: int

many_dataclasses = []
for i in range(1000):
    many_dataclasses.append({
        'city': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
        'tariffs': [
            RecordDataClass(
               shop_id=random.randint(1, 10000),
               delivery_days=random.randint(1, 12),
               delivery_price=random.randint(125, 888)
            ) for _ in range(3)
        ]
    })
print(f'List[Dataclass], размер в памяти: '
      f'{humanize_bytes(asizeof.asizeof(many_dataclasses))}')
