/*
init.nsh

Initialization functions
*/

#--------------------------------
# User initialization

#--------------------------------
# visible installer sections

Section "!${APP_NAME}" SecCore
 SectionIn RO
SectionEnd

#Section "Desktop icon" SecDesktop
# StrCpy $CreateDesktopIcon "true"
#SectionEnd

# Section descriptions
#!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
#!insertmacro MUI_DESCRIPTION_TEXT ${SecCore} "$(SecCoreDescription)"
#!insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "Create icon on the desktop."
#!insertmacro MUI_FUNCTION_DESCRIPTION_END


# .onInit must be here after the section definition because we have to set
# the selection states of the dictionary sections
Function .onInit

  # check if it is a 64bit system
  ${if} ${RunningX64}
   SetRegView 64
   !define LIBRARY_X64
  ${endif}
  
  # initialize the multi-user installer UI
  !insertmacro MULTIUSER_INIT
FunctionEnd

# this function is called at first after starting the uninstaller
#Function un.onInit
#  !insertmacro MULTIUSER_UNINIT
#FunctionEnd
