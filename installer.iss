[Setup]
AppName=Auto Screen Frequency
AppVersion=1.1
DefaultDirName={autopf}\AutoScreenFrequency
OutputBaseFilename=AutoScreenFrequencyInstall
SignTool=MsSign $f

[Languages]
Name: "ru"; MessagesFile: "compiler:Languages\Russian.isl"

[Files]
Source: "output/AutoScreenFrequency.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Auto Screen Frequency"; Filename: "{app}\AutoScreenFrequency.exe"; WorkingDir: "{app}"

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "AutoScreenFrequency"; ValueData: "{app}\AutoScreenFrequency.exe"; Flags: uninsdeletevalue
Root: HKCU; Subkey: "Software\AutoScreenFrequency"; Flags: uninsdeletevalue

[Run]
Filename: "{app}\AutoScreenFrequency.exe"; Description: "Запустить приложение"; Flags: nowait postinstall
