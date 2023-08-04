import logging
import os


logging.basicConfig(
    level=os.environ.get('LOGLEVEL', logging.INFO),
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)
