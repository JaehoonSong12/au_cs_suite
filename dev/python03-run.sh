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
else
    echo "Unsupported OS type: $OSTYPE"
    exit 1
fi
############################################
########## Shell Script (Scripts) ##########
############################################
poetry run python cli.py
# poetry run python gpb_server/cli/app.py
# poetry run python gui.py
# poetry run python gpb_server/gui/app.py