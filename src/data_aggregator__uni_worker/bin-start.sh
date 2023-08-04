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



# ARGS
# ======================================================================================================

APPLICATION_RELOAD="${APPLICATION_RELOAD:-0}"

echo "APPLICATION_RELOAD=${APPLICATION_RELOAD}"


# RUN
# ======================================================================================================

if [ "${APPLICATION_RELOAD}" == "0" ]; then
    echo "NORMAL START"
    ${THIS_DIR}/bin-just-start.sh
else
    echo "RELOAD START"
    watchmedo auto-restart --pattern=*.py --recursive --directory=./src ${THIS_DIR}/bin-just-start.sh
fi
