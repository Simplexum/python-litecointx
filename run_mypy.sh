#!/usr/bin/env sh
#-*-mode: sh; encoding: utf-8-*-

_MY_DIR="$( cd "$( dirname "${0}" )" && pwd )"
set -ex
[ -d "${_MY_DIR}" ]
[ "${_MY_DIR}/run_mypy.sh" -ef "${0}" ]
cd "${_MY_DIR}"

mypy --strict `find ./litecointx -path ./litecointx/tests -prune -o -name "*.py" -print|sort`
mypy `find ./litecointx/tests -name "*.py" -print|sort`
