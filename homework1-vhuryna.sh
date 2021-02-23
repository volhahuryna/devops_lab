#!/bin/bash

set +e

pyenv install 2.7.18 &> /dev/null
pyenv install 3.7.0 &> /dev/null
pyenv virtualenv 2.7.18 venv-2.7
pyenv virtualenv 3.7.0 venv-3.7
