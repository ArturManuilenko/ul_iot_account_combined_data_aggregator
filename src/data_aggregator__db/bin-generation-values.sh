#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"

set -o errexit
set -o pipefail
set -o nounset



# INIT WORKING DIR
# ======================================================================================================
cd "$(dirname "${BASH_SOURCE[0]}")"
THIS_DIR="$(pwd)"
cd ../../
CWD="$(pwd)"

python3 -m src.data_aggregator__db.generation_values
