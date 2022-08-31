/*
declaration.nsh

Configuration and variables of FreeCAD installer
*/

#--------------------------------
# File locations

#!define FILES_LICENSE "license.rtf"

#--------------------------------
# Names and version

!define APP_NAME "CETONI_Elements_Documentation"
!define APP_VERSION_NUMBER "${APP_VERSION_MAJOR}.${APP_VERSION_MINOR}.${APP_VERSION_REVISION}.${APP_VERSION_BUILD}"
!define APP_DIR "${APP_NAME}"
#!define APP_REGKEY "Software\${APP_NAME}" 
#!define APP_REGKEY_SETUP "${APP_REGKEY}\Setup"
#!define APP_REGKEY_SETTINGS "${APP_REGKEY}\Settings"


#--------------------------------
# Setup settings
!define SETUP_EXE ${ExeFile}

