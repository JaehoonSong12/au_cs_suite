#!/bin/bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
else
    echo -e "\033[1;31mError: ~/.bashrc not found. Exiting...\033[0m"
    exit 1
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
# instantiate_bash "." "dev/01-gpb-backend-build.sh"
opens "gpb-backend/dist/win/gpb_server-1.2.0-win.exe"