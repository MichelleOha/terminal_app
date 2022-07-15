#!/bin/bash

if ! [[ -x "$(command -v python)"]]: then
   echo 'Python not installed: Please install Python3 by visiting this website https://installpython3.com which will then allow you to run the application.'
   exit 1
fi

    python3 mywardrobe.py

