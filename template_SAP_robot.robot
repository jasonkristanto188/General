*** Settings ***
Library    creds.py
Library    datetime_custom.py

Library    SapGuiLibrary
Library    RPA.Windows

*** Variables ***
${CONNECTION NAME}=    01. ADM S/4 HANA Production
# ${CONNECTION NAME}=    04. ADM S/4 Hana Simulation
${CLIENT}=    310    
${SAP USERNAME}=    
${SAP PASSWORD}=    

*** Tasks ***
Main
    SapGuiLibrary.Disable Screenshots On Error
    Get Credentials
    Login SAP
    SAP Run Transaction    /nFBL3N
    
*** Keywords ***
Get Credentials
    ${username}=    Get Username
    Set Suite Variable    ${SAP USERNAME}    ${username}

    ${password}=    Get Password
    Set Suite Variable    ${SAP PASSWORD}    ${password}

Get Credentials For SAP Via CMD
    Clear CMD
    Log To Console    ${\n}Enter your username:
    ${username}=    Get User Input    Enter your username:
    Set Suite Variable    ${SAP USERNAME}    ${username}
    Clear CMD
    Log To Console    ${\n}Enter your password:
    ${password}=    Get User Input    Enter your password:
    Set Suite Variable    ${SAP PASSWORD}    ${password}
    Clear CMD

Login SAP
    Windows Run    C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe
    Sleep    1
    SapGuiLibrary.Connect To Session    
    Sleep    10
    SapGuiLibrary.Open Connection   ${CONNECTION NAME}
    Sleep    5
    SapGuiLibrary.Input Text        wnd[0]/usr/txtRSYST-MANDT    ${CLIENT}
    SapGuiLibrary.Input Text        wnd[0]/usr/txtRSYST-BNAME    ${SAP USERNAME}
    SapGuiLibrary.Input Password    wnd[0]/usr/pwdRSYST-BCODE    ${SAP PASSWORD}
    SapGuiLibrary.Input Text        wnd[0]/usr/txtRSYST-LANGU    EN
    SapGuiLibrary.Send Vkey         0
    Sleep    2
    # If system message occurs during login
    TRY
        SapGuiLibrary.Click Element    /app/con[0]/ses[0]/wnd[1]/tbar[0]/btn[12]
    EXCEPT    
        Log To Console    No system message found during login
    END
 
    Log To Console    logged into SAP

SAP Run Transaction
    [Arguments]    ${saptransaction}
 
    ${transactionvalidcheck}=    Run Keyword And Return Status    Should Start With    ${saptransaction}    /n
    IF    ${transactionvalidcheck} == ${False}
        ${saptransaction}=    Catenate    SEPARATOR=    /n    ${saptransaction}
    END
 
    SapGuiLibrary.Set Focus    /app/con[0]/ses[0]/wnd[0]/tbar[0]/okcd
    Sleep    1
    SapGuiLibrary.Run Transaction    ${saptransaction}
    Sleep    1
