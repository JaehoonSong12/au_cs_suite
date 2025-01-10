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
        INIT_NODE
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then                              # macOS
    python --version
    pip --version
    python3 --version
    pip3 --version
    node -v
    npm -v
    npx -v
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




COMMON_DIST="$PWD/distribution"
rm -rf "$COMMON_DIST" && mkdir -p "$COMMON_DIST"

# List of projects
PROJECTS=(
    # "gpb_client" 
    "gpb-backend" 
    "gpb-frontend-admin"
)

# Loop through each project and copy its dist folder
for PROJECT in "${PROJECTS[@]}"; do
  DIST_FOLDER="$PROJECT/dist"
  cp -r "$DIST_FOLDER/"* "$COMMON_DIST/"
done


if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then          # Windows
    opens "${COMMON_DIST}/win"
elif [[ "$OSTYPE" == "darwin"* ]]; then                              # macOS
    opens "${COMMON_DIST}/osx"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then                           # Linux
    opens "${COMMON_DIST}/lnx"
else
    echo "Unsupported OS type: $OSTYPE"
    exit 1
fi

# instantiate_bash "." "dev/01-gpb-backend-build.sh"