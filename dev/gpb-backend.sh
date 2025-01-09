#!/bin/bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
else
    echo -e "\033[1;31mError: ~/.bashrc not found. Exiting...\033[0m"
    exit 1
fi
# /usr

cd gpb-backend




# Extract the 'name' field and 'version' field
name=$(grep -oP '(?<=^name = ").*(?=")' pyproject.toml)
version=$(grep -oP '(?<=^version = ").*(?=")' pyproject.toml)

entry="gpb_server/app/__main__.py"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then          # Windows
    outputPath="./dist/win"
    outputFile="${name}-${version}-win"
    if ! python --version 2>/dev/null && ! python3 --version 2>/dev/null; then
        INIT_PVM
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then                              # macOS
    outputPath="./dist/osx"
    outputFile="${name}-${version}-osx"
    python --version
    pip --version
    python3 --version
    pip3 --version
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then                           # Linux
    echo "Detected Linux: $OSTYPE"
    outputPath="./dist/lnx"
    outputFile="${name}-${version}-lnx"
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
## clean
poetry env remove python
rm poetry.lock
rm -rf build
rm -rf dist
## init
pipreqs . --ignore "ext/" --force   # dependency generate
poetry add $(cat requirements.txt)  # dependency control
rm requirements.txt                 # clean 
poetry install
## build
poetry build
poetry run pyinstaller --distpath ${outputPath} --name ${outputFile} --onefile ${entry}
rm *.spec                 # clean 
# < Installation >
# pip install dist/gpb_server-1.2.0-py3-none-any.whl
#   gpb
#   gpb_cli
#   gpb_gui
# < Publication >
# poetry publish