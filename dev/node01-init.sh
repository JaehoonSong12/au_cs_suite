#!/bin/bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
# /usr
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then          # Windows
    if ! node -v 2>/dev/null; then
        INIT_NODE
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then                              # macOS
    node -v
    npm -v
    npx -v
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
cd gpb_client_test
npm install axios                           # npm install
npm start
cd ..