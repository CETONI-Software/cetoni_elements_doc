/*

Settings for installer

These typically need to be modified for each release

*/

# Make the installer as small as possible
# comment this for testing builds since it will reduce the time to create an installer
# a lot - for the cost of a much greater file size.
# So assure it is active for release builds!
SetCompressor /SOLID lzma

#--------------------------------
# Version number

!define APP_VERSION_MAJOR 0
!define APP_VERSION_MINOR 20
!define APP_VERSION_REVISION 0
!define APP_VERSION_BUILD 0
!define APP_INFO "CETONI Elements Documentation"

!define APP_VERSION "${APP_VERSION_MAJOR}.${APP_VERSION_MINOR}.${APP_VERSION_REVISION}" # Version to display

!define COPYRIGHT_YEAR 2022
!define COMPANY "CETONI GmbH"

#--------------------------------
# Installer file name
!define ExeFile "${APP_NAME}_Installer.exe"

#--------------------------------
# installer bit type - only provided as 64bit build
!define MULTIUSER_USE_PROGRAMFILES64

#--------------------------------
# File locations
# !!! you need to adjust them to the folders in your Windows system !!!
!define PROJECT_DIR ..
