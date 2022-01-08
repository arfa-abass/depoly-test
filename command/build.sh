#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

pip  install  -r requirements/dev.txt
python manage.py migrate
