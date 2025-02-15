#!/bin/bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
else
    echo -e "\033[1;31mError: ~/.bashrc not found. Exiting...\033[0m"
    exit 1
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
cd gpb_client_admin                          # Admin Mode
# cd gpb_client                             # Client Mode



npm install
npm run build


# pkg server.js --output app-executable
# pkg server.js --output app-executable --targets node18-win-x64,node18-macos-x64,node18-macos-arm64


cd ..