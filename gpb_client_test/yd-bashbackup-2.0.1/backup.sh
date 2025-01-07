#!/bin/bash
EXT_DIR_ABS="$(pwd)/ext"
JDK_VERSIONS=("17")
JDK_IDENTIFIERS=("0d483333a00540d886896bac774ff48b")
JDK_URL="https://download.java.net/java/GA/jdk{VERSION}/{IDENTIFIER}/35/GPL/openjdk-{VERSION}_windows-x64_bin.zip"
JDK_DIR="${EXT_DIR_ABS}/jdk-{VERSION}/bin"
if [ -d "${EXT_DIR_ABS}" ]; then
    echo "Directory ${EXT_DIR_ABS} already exists. Skipping installation."
else
    echo "Directory ${EXT_DIR_ABS} does not exist. Proceeding with installation."
    # Initialize JDK
    for i in "${!JDK_VERSIONS[@]}"; do
        ver="${JDK_VERSIONS[$i]}"
        identifier="${JDK_IDENTIFIERS[$i]}"
        url="${JDK_URL//\{VERSION\}/$ver}"
        url="${url//\{IDENTIFIER\}/$identifier}"
        echo -e "Downloading jdk.zip..."
        curl -L "$url" -o "jdk.zip"
        echo -e "Extracting jdk.zip..."
        mkdir -p "${EXT_DIR_ABS}"
        unzip "jdk.zip" -d "${EXT_DIR_ABS}"
        echo -e "Finished initialization of jdk.zip..."
        rm "jdk.zip"
    done
fi

# Set up JDK environment
for ver in "${JDK_VERSIONS[@]}"; do
    export JAVA_HOME="${EXT_DIR_ABS}/jdk-${ver}"
    export PATH="${JAVA_HOME}/bin:${PATH}"
done

# Check versions
java -version
echo "JAVA_HOME: $JAVA_HOME"








#################################################
# Backup in cs3510 subdirectory
#################################################
WORKING_DIR="cs3510"
cd $WORKING_DIR
../yd-bashbackup-2.0.1/bin/app.bat