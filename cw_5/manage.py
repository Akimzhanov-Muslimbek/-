#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cw_5.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Если Django не установлен, вывести сообщение об ошибке.
        raise ImportError(
            "Django не установлен. Пожалуйста, установите Django и повторите попытку."
        )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
