/*
Installer for Windows
Author: Uwe Kindler
Compatible with NSIS 3.x
*/

# Do a Cyclic Redundancy Check to make sure the installer
# was not corrupted by the download.
CRCCheck on

# make it a Unicode installer
Unicode true

# enable support for high DPI resolution
ManifestDPIAware true

# installer settings like version numbers
!include settings.nsh

# declarations of FreeCAD's registry keys
!include declarations.nsh

# Multi-User settings
!define MULTIUSER_EXECUTIONLEVEL User
#!define MULTIUSER_INSTALLMODE_DEFAULT_REGISTRY_KEY "${APP_REGKEY}"
#!define MULTIUSER_INSTALLMODE_DEFAULT_REGISTRY_VALUENAME ""

!define MULTIUSER_INSTALLMODE_INSTDIR "${APP_DIR}"
#!define MULTIUSER_INSTALLMODE_INSTDIR_REGISTRY_KEY "${APP_REGKEY}"
#!define MULTIUSER_INSTALLMODE_INSTDIR_REGISTRY_VALUENAME ""

#!define MULTIUSER_INSTALLMODE_FUNCTION InitUser
!define MULTIUSER_MUI

# included NSIS files
#!include InstallOptions.nsh
#!include LangFile.nsh
#!include Library.nsh
#!include LogicLib.nsh
!include MUI2.nsh
!include MultiUser.nsh
!include Sections.nsh
!include WinVer.nsh
!include x64.nsh


# Set of various macros and functions
#!include include\utils.nsh

# Configure start of documentation after install
!define MUI_FINISHPAGE_RUN
!define MUI_FINISHPAGE_RUN_TEXT "Show CETONI Elements Manual"
!define MUI_FINISHPAGE_RUN_FUNCTION "LaunchLink"

Function LaunchLink
  ExecShell "" "$INSTDIR\Manual_EN\index.html"
FunctionEnd

# set up the installer pages
!include gui.nsh

# sets the install sections and checks the system on starting the un/installer
!include init.nsh

# install app and needed third-party programs like Python etc.
!include install.nsh

# uninstall app and all programs that were installed together with FreeCAD
#!include setup\uninstall.nsh

# configure app (set start menu and write registry entries)
#!include setup\configure.nsh

#--------------------------------
# Output file
Outfile "${SETUP_EXE}"

# sign the installer executable
#!finalize 'signing.bat ${SETUP_EXE}'
