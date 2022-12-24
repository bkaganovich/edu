## Lab 2

Date: `Thu 22 Dec 2022 06:25 IST`

## Files and SHA-256 checksums

```
f09ffe74770a7229ddef667bc95fa73e0886adf8739cdfff36101443975e5b5a    financials-xls.exe
```

# Questions:
```
1.  Upload the files to http://www.VirusTotal.com/ and view the reports. Does 
    either file match any existing antivirus signatures?
2.  When were these files compiled?
3.  Are there any indications that either of these files is packed or 
    obfuscated? If so, what are these indicators?
4.  Do any imports hint at what this malware does? If so, which imports are 
    they?
5.  Are there any other files or host-based indicators that you could look for 
    on infected systems?
6.  What network-based indicators could be used to find this malware on 
    infected machines?
7.  Can you guess what is the purpose of the malware?
```

[1]: https://www.virustotal.com/gui/file/f09ffe74770a7229ddef667bc95fa73e0886adf8739cdfff36101443975e5b5a/details
[2]: https://www.virustotal.com/gui/file/f09ffe74770a7229ddef667bc95fa73e0886adf8739cdfff36101443975e5b5a/behavior
[3]: https://www.virustotal.com/gui/file/f09ffe74770a7229ddef667bc95fa73e0886adf8739cdfff36101443975e5b5a/relations

# 1. [virustotal.com](https://virustotal.com) [[1]]

```
59/72 detection
59 security vendors and 1 sandbox flagged this file as malicious
```

# 2. Details > History:

### `financials-xls.exe` [[1]]

```
Creation Time	2007-05-07 12:58:10 UTC
```

# 3. Obfuscated/packed?

# 4. Details > Imports, what malware does:

### `financials-xls.exe` [[1]]

```
ADVAPI32.dll
    RegCloseKey

KERNEL32.DLL
    ExitProcess 
    GetProcAddress 
    LoadLibraryA 
    VirtualProtect

WSOCK32.dll
    sendto

SHELL32.dll
    Shell_NotifyIconA

ole32.dll
    CoInitialize

USER32.dll
    IsChild

COMCTL32.dll
    InitCommonControlsEx
```


# 5. Other files or indicators on infected system:

## Behavior > Process And Service Actions > Processes Tree:

### `financials-xls.exe` [[2]]

```
1120 - file.exe
2304 - <PATH_SAMPLE.EXE>
2384 - 'C:\Windows\xpupdate.exe'
2688 - %WINDIR%\explorer.exe
3200 - 'C:\Windows\xpupdate.exe'
 -> 3980 - %SAMPLEPATH%\f09ffe74770a7229ddef667bc95fa73e0886adf8739cdfff36101443975e5b5a.exe
7592 - 'C:\Windows\xpupdate.exe'
7912 - 'C:\Users\user\Desktop\executable.exe'
8096 - 'C:\Windows\xpupdate.exe'
```

## Behavior > File System Actions > Files Dropped:

### `financials-xls.exe` [[2]]

```
%USERPROFILE%\AppData\Local\Temp\{04AAD741-F8DC-49E2-925B-2EAB17BF5360}.png
%USERPROFILE%\AppData\Local\Temp\{12E15329-953D-430D-952C-99C576ECB387}.png
%USERPROFILE%\AppData\Local\Temp\{25115AE5-09E1-4646-AAF2-2C31226E0B67}.png
%USERPROFILE%\AppData\Local\Temp\{41D64EBB-6268-4D94-A5F3-3F0A453A6BCF}.png
%USERPROFILE%\AppData\Local\Temp\{43A8F4D4-70CC-468B-AA69-16E140DF870A}.png
%USERPROFILE%\AppData\Local\Temp\{5D633D69-9BDE-44E6-BE54-45B663D4D008}.png
%USERPROFILE%\AppData\Local\Temp\{5D687947-2737-4174-B4F4-55858F81DC7D}.png
%USERPROFILE%\AppData\Local\Temp\{706A5792-1A25-4EB0-B3B9-6F7B752466ED}.png
%USERPROFILE%\AppData\Local\Temp\{81AFD8F4-A2E8-49F0-AF6B-F1696612FBFC}.png
%USERPROFILE%\AppData\Local\Temp\{86583635-145A-4C45-A1F8-5D4054F14452}.png
%USERPROFILE%\AppData\Local\Temp\{8C8E81FE-BDB6-4742-8EF7-B0B500D2504B}.png
%USERPROFILE%\AppData\Local\Temp\{997A560C-83C4-476D-BE63-8C952AB1E07D}.png
%USERPROFILE%\AppData\Local\Temp\{9A91699F-6EF5-446A-AD04-662CB452D12F}.png
%USERPROFILE%\AppData\Local\Temp\{CD33F607-B44F-4B53-B044-5F3AF18F3D3E}.png
%USERPROFILE%\AppData\Roaming\Install.dat
%WINDIR%\xpupdate.exe
C:\ProgramData\Microsoft\Windows\WER\Temp\WER10A4.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER10A4.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER145E.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER145E.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER14DC.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER14DC.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER269D.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER269D.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2769.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2769.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER27A8.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER27A8.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2B60.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2B60.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2C1C.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2C1C.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2C4C.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER2C4C.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER319B.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER319B.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER319C.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER319C.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER31AD.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER31AD.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER3E8A.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER3E8A.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER3E8C.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER3E8C.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER3E9D.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER3E9D.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER44C4.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER44C4.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER44D6.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER44D6.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER44D7.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER44D7.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER4ED6.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER4ED6.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER4EE8.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER4EE8.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER4EF9.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER4EF9.tmp.txt
C:\ProgramData\Microsoft\Windows\WER\Temp\WER579.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER579.tmp.WERInternalMetadata.xml
C:\ProgramData\Microsoft\Windows\WER\Temp\WER644.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER644.tmp.csv
C:\ProgramData\Microsoft\Windows\WER\Temp\WER693.tmp
C:\ProgramData\Microsoft\Windows\WER\Temp\WER693.tmp.txt
C:\Sysmon\438274944D21C3590AB2F6C5A34D5933B808ACB6409037FFE5B95B31EF18E8BDCFC6B5E6A0049489ADC5CECAFC7F95524157170C3CDA66F72AD85350D09F0476432071D000000000000000000000000000000000
C:\Windows\ServiceProfiles\LocalService\AppData\Roaming\Microsoft\Crypto\Keys\de7cf8a7901d2ad13e5c67c29e5d1662_cbbb49d6-b7ff-44ca-aba5-8a5e250d4d42
C:\Windows\System32\Microsoft\Protect\S-1-5-18\User\87dffc4f-e3b2-49ec-bed9-3f6d2cf7e6df
C:\Windows\System32\spp\store\2.0\cache\cache.dat
C:\Windows\System32\spp\store\2.0\data.dat.tmp
C:\Windows\xpupdate.exe
C:\Windows\xpupdate.exe:Zone.Identifier
```

## Behavior > Registry Actions > Registry Keys Set:

### `financials-xls.exe` [[2]]

```
<HKCU>\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Windows update loader
HKEY_CURRENT_USER\SOFTWARE\Install
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\Windows update loader
HKLM\SOFTWARE\Microsoft\Windows Media Player NSS\3.0\Servers\A70D59A1-8EAD-4F40-AAAB-FBFC460800A4\FriendlyName
HKU\%SID%\Software\Microsoft\Windows\CurrentVersion\Run\Windows update loader
HKU\S-1-5-21-3711686801-687107597-1149503783-1001\Software\Microsoft\Windows\CurrentVersion\Run\Windows update loader
SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Windows update loader
\REGISTRY\USER\S-1-5-21-1482476501-1645522239-1417001333-500\Software\Microsoft\Windows\CurrentVersion\Run\Windows update loader
```

## Relations:

### `financials-xls.exe` [[3]]

```
Execution Parents: 4
Bundled Files: 1
Dropped Files: 2
```

# 6. Network based indicators to find on infected machine


## Behavior > Network Communication > DNS Resolutions:

### `financials-xls.exe` [[2]]

```
dns.msftncsi.com
131.107.255.255
login.live.com
40.126.31.139
20.190.159.134
20.190.159.138
40.126.31.137
40.126.31.4
40.126.31.1
40.126.31.141
40.126.31.143
```

## Behavior > Network Communication > IP Traffic:

### `financials-xls.exe` [[2]]

```
13.107.4.50:80 (TCP)
20.80.129.13:443 (TCP)
20.99.132.105:443 (TCP)
20.99.184.37:443 (TCP)
23.216.147.64:443 (TCP)
23.216.147.76:443 (TCP)
69.50.175.181:80
69.50.175.181:80 (TCP)
<MACHINE_DNS_SERVER>:53 (UDP)
a83f:8110:1616:16ff:1616:16ff:1717:17ff:53 (UDP)
```

## Relations > Contacted Domains:

### `financials-xls.exe` [[3]]

```
dns.msftncsi.com
login.live.com
```

## Relations > Contacted IP Addresses:

### `financials-xls.exe` [[3]]

```
13.107.4.50
131.107.255.255
20.190.159.134
20.190.159.138
20.80.129.13
20.99.132.105
20.99.184.37
23.216.147.64
23.216.147.76
40.126.31.1
40.126.31.137
40.126.31.139
40.126.31.141
40.126.31.143
40.126.31.4
69.50.175.181
```

# 7. What is the purpose of the files?

https://www.hybrid-analysis.com/sample/f09ffe74770a7229ddef667bc95fa73e0886adf8739cdfff36101443975e5b5a