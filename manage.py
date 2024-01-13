#!/usr/bin/ env python3
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web3.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            ''' Django import failed.
                Please ensure that Django is installed and accessible on your PYTHONPATH environment variable.
                Have you activated a virtual environment?"
            '''
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
