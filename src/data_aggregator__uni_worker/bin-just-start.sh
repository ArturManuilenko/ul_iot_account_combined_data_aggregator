#!/bin/bash

echo ">>> $(basename ${BASH_SOURCE[0]})"

set -o errexit
set -o pipefail
set -o nounset

# INIT WORKING DIR
# ======================================================================================================
cd "$(dirname "${BASH_SOURCE[0]}")"
cd ../../
CWD="$(pwd)"

# ENV
# ======================================================================================================

export PYTHONUNBUFFERED=1
export PYTHONPATH="${CWD}"

# RUN
# ======================================================================================================

python3 -m src.data_aggregator__uni_worker.run --worker=${WORKER_NAME}
