import logging
import os


logging.basicConfig(
    level=os.environ.get('LOGLEVEL', logging.INFO),
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)

logging.getLogger("unipipeline").setLevel(logging.DEBUG)
logging.getLogger('api_utils').setLevel(logging.DEBUG)

self_logging = logging
