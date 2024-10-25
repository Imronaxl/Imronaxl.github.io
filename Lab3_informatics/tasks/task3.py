import re

def solve(cron_expression):
    # Определяем регулярное выражение для проверки формата cron-выражений
    cron_pattern = re.compile(
        r'^(?:'                       # Начало строки
        r'(\*|(?:[0-5]?[0-9]|[1-5][0-9])) '  # Минуты
        r'(\*|(?:[01]?[0-9]|2[0-3])) '       # Часы
        r'(\*|(?:[1-9]|[12][0-9]|3[01])) '  # Дни месяца
        r'(\*|(?:[1-9]|1[0-2]|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)) '  # Месяцы
        r'(\*|(?:[0-6]|sun|mon|tue|wed|thu|fri|sat))'  # Дни недели
        r')$'                         # Конец строки
    )

    return bool(cron_pattern.match(cron_expression))


