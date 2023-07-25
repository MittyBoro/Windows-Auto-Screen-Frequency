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

; pyinstaller --noconfirm --onefile --windowed --icon "./src/favicon.ico" --name "Auto Screen Frequency" --disable-windowed-traceback  "./app.py"
; "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\signtool.exe" sign /tr http://timestamp.digicert.com /td sha256 /fd sha256 /a $p
