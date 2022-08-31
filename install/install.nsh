/*

install.nsh

Installation of program files, dictionaries and external components

*/

#--------------------------------
# Program files

Section -ProgramFiles SecProgramFiles
    SetOverwrite on
    SetOutPath $INSTDIR\Handbuch_DE
    File /r ${PROJECT_DIR}\CETONI_Elements_Manual_DE\_build\html\*

    SetOutPath $INSTDIR\Manual_EN
    File /r ${PROJECT_DIR}\CETONI_Elements_Manual_EN\_build\html\*
SectionEnd
