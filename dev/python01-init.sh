#!/bin/bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
# /usr
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then          # Windows
    if ! python --version 2>/dev/null && ! python3 --version 2>/dev/null; then
        INIT_PVM
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then                              # macOS
    python --version
    pip --version
    python3 --version
    pip3 --version
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then                           # Linux
    echo "Detected Linux: $OSTYPE"
    # Add Linux-specific commands here if needed
    exit 1
else
    echo "Unsupported OS type: $OSTYPE"
    exit 1
fi
############################################
########## Shell Script (Scripts) ##########
############################################
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
    PIP_CMD=pip
else
    echo -e "${RED}Python is not installed. Please install Python and try again.${NC}"
    exit 1
fi
if ! command -v poetry &>/dev/null; then
    echo -e "\033[0;33mpoetry is not installed. Installing...\033[0m"
    $PIP_CMD install poetry
fi
if ! command -v tox &>/dev/null; then
    echo -e "\033[0;33mtox is not installed. Installing...\033[0m"
    $PIP_CMD install tox
fi
if ! command -v pipreqs &>/dev/null; then
    echo -e "\033[0;33mpipreqs is not installed. Installing...\033[0m"
    $PIP_CMD install pipreqs
fi
pipreqs . --ignore "ext/" --force   # dependency generate
poetry add $(cat requirements.txt)  # dependency control
rm requirements.txt                 # clean 
poetry run pip install python-multipart