import os

from unipipeline.modules.uni import Uni

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dag.yml")

uni = Uni(CONFIG_FILE)
