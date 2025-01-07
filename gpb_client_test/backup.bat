@echo off

REM Hardcoded values
set "EXT_DIR_ABS=%cd%\ext"
set "JDK_VERSION=17"
set "JDK_IDENTIFIER=0d483333a00540d886896bac774ff48b"
set "JDK_URL=https://download.java.net/java/GA/jdk%JDK_VERSION%/%JDK_IDENTIFIER%/35/GPL/openjdk-%JDK_VERSION%_windows-x64_bin.zip"
set "JDK_DIR=%EXT_DIR_ABS%\jdk-%JDK_VERSION%\bin"

if exist "%EXT_DIR_ABS%" (
    echo Directory %EXT_DIR_ABS% already exists. Skipping installation.
) else (
    echo Directory %EXT_DIR_ABS% does not exist. Proceeding with installation.
    echo Downloading jdk.zip...
    curl -L "%JDK_URL%" -o "jdk.zip"
    echo Extracting jdk.zip...
    mkdir "%EXT_DIR_ABS%"
    tar -xf "jdk.zip" -C "%EXT_DIR_ABS%"
    echo Finished initialization of jdk.zip...
    del "jdk.zip"
)

REM Set up JDK environment
set "JAVA_HOME=%EXT_DIR_ABS%\jdk-%JDK_VERSION%"
set "PATH=%JAVA_HOME%\bin;%PATH%"

REM Check versions
java -version
echo JAVA_HOME: %JAVA_HOME%
call pause

set "WORKING_DIR=cs3510"
cd %WORKING_DIR%
..\yd-bashbackup-2.0.1\bin\app.bat