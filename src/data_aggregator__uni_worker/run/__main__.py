from argparse import ArgumentParser

import src.conf.self_logging  # noqa
from src.data_aggregator__uni_worker.lib import uni

parser = ArgumentParser()
parser.add_argument('--worker', required=True, type=str)
args = parser.parse_args()

uni.check()
uni.init_consumer_worker(args.worker)
uni.initialize()
uni.start_consuming()
