## Lab01-01

Date: `Thu 22 Dec 2022 06:24 IST`

## Files and SHA-256 checksums

```
f50e42c8dfaab649bde0398867e930b86c2a599e8db83b8260393082268f2dba  Lab01-01.dll
58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47  Lab01-01.exe
```

# Questions:

```
1.  Upload the files to http://www.VirusTotal.com/ and view the reports. Does 
    either file match any existing antivirus signatures?
2.  When were these files compiled?
3.  Are there any indications that either of these files is packed or 
    obfuscated? If so, what are these indicators?
4.  Do any imports hint at what this malware does? If so, which imports are they?
5.  Are there any other files or host-based indicators that you could look for 
    on infected systems?
6.  What network-based indicators could be used to find this malware on 
    infected machines?
7.  What would you guess is the purpose of these files?
```

[1]: https://www.virustotal.com/gui/file/f50e42c8dfaab649bde0398867e930b86c2a599e8db83b8260393082268f2dba/details
[3]: https://www.virustotal.com/gui/file/f50e42c8dfaab649bde0398867e930b86c2a599e8db83b8260393082268f2dba/behavior

[2]: https://www.virustotal.com/gui/file/58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47/details
[4]: https://www.virustotal.com/gui/file/58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47/behavior
[6]: https://www.virustotal.com/gui/file/58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47/relations


# 1. [virustotal.com](https://virustotal.com)

### `Lab01-01.dll` [[1]]

```
40 security vendors and no sandboxes flagged this file as malicious
Score: 40/69
```

### `Lab01-01.exe` [[2]]

```
51 security vendors and 1 sandbox flagged this file as malicious
Score: 51/71
```

# 2. Details > History:

### `Lab01-01.dll` [[1]]

```
Creation Time	2010-12-19 16:16:38 UTC
```

### `Lab01-01.exe` [[2]]

```
Creation Time	2010-12-19 16:16:19 UTC
```

# 3. Obfuscated/packed?

No information available

# 4. Details > Imports, what malware does:

Searches for and copies files, creates processes, and operates over a network.

### `Lab01-01.dll` [[1]]

```
KERNEL32.dll
    CloseHandle 
    CreateMutexA 
    CreateProcessA 
    OpenMutexA 
    Sleep

MSVCRT.dll
    _adjust_fdiv 
    _initterm 
    free 
    malloc 
    strncmp

WS2_32.dll
    closesocket 
    connect 
    htons 
    inet_addr 
    recv 
    send 
    shutdown 
    socket 
    WSACleanup 
    WSAStartup
```

### `Lab01-01.exe` [[2]]

```
KERNEL32.dll
    CloseHandle
    CopyFileA
    CreateFileA
    CreateFileMappingA
    FindClose
    FindFirstFileA
    FindNextFileA
    IsBadReadPtr
    MapViewOfFile
    UnmapViewOfFile

MSVCRT.dll
    __getmainargs 
    __p___initenv 
    __p__commode 
    __p__fmode 
    __set_app_type 
    __setusermatherr 
    _adjust_fdiv 
    _controlfp 
    _except_handler3 
    _exit
```

# 5. Other files or indicators on infected system:

## Behavior > Process And Service Actions > Processes Tree:

### `Lab01-01.dll` [[3]]

```
2288 - %windir%\System32\svchost.exe -k WerSvcGroup
2696 - %SANDBOX_DLL_LOADER_X86% %SAMPLEPATH% %WORKDIR% 483
2964 - wmiadap.exe /F /T /R
3008 - %windir%\system32\wbem\wmiprvse.exe
```

### `Lab01-01.exe` [[4]]

```
1068 - 'C:\Users\user\Desktop\software.exe'
1468 - ****.exe
2200 - %windir%\System32\svchost.exe -k WerSvcGroup
2612 - %SAMPLEPATH%
2680 - %CONHOST% "1392043765-1395574979-349962065-902790045209994247612312528943713311251798354134
2904 - wmiadap.exe /F /T /R
2944 - %windir%\system32\wbem\wmiprvse.exe
 -> 3768 - %SAMPLEPATH%\58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47.exe
3820 - %WINDIR%\explorer.exe
 -> 6068 - C:\Windows\System32\conhost.exe C:\Windows\system32\conhost.exe 0xffffffff -ForceV1
```

## Behavior > File System Actions > Files Dropped:

### `Lab01-01.exe` [[4]]

## Behavior > Registry Actions > Registry Keys Set:

### `Lab01-01.exe` [[4]]

## Relations:

### `Lab01-01.exe` [[6]]

```
Execution Parents: 33
PE Resource Parents: 5
Bundled Files: 3
Dropped Files: 379 
```

# 6. Network based indicators to find on infected machine

## Behavior > Network Communication > DNS Resolutions:

### `Lab01-01.exe` [[4]]

```
12.179.89.13.in-addr.arpa
128.233.212.23.in-addr.arpa
147.251.123.92.in-addr.arpa
150.32.88.40.in-addr.arpa
152.251.123.92.in-addr.arpa
154.210.82.20.in-addr.arpa
20.173.189.20.in-addr.arpa
201.198.147.52.in-addr.arpa
202.64.54.20.in-addr.arpa
212.143.182.52.in-addr.arpa
212.57.85.104.in-addr.arpa
216.29.43.23.in-addr.arpa
22.173.189.20.in-addr.arpa
23.42.107.13.in-addr.arpa
26.37.247.52.in-addr.arpa
4.31.126.40.in-addr.arpa
44.168.124.40.in-addr.arpa
58.142.123.92.in-addr.arpa
62.102.50.20.in-addr.arpa
72.238.56.23.in-addr.arpa
8.160.190.20.in-addr.arpa
82.250.63.168.in-addr.arpa
83.188.255.52.in-addr.arpa
86.232.212.23.in-addr.arpa
97.148.17.2.in-addr.arpa
msftstore.s.llnwi.net
sfd-production.azurefd.net
windowsupdatebg.s.llnwi.net
www.microsoft.com
```

## Behavior > Network Communication > IP Traffic:

### `Lab01-01.exe` [[4]]

```
104.86.182.43:443 (TCP)
104.97.41.163:80 (TCP)
13.107.39.203:80 (TCP)
13.107.4.50:80 (TCP)
131.253.33.203:80 (TCP)
168.62.242.76:443 (TCP)
185.125.188.58:443 (TCP)
185.125.190.44:443 (TCP)
185.125.190.45:443 (TCP)
192.168.0.11:137 (UDP)
192.168.0.137:137 (UDP)
192.168.0.14:137 (UDP)
192.168.0.150:137 (UDP)
192.168.0.15:137 (UDP)
192.168.0.1:137 (UDP)
192.168.0.21:137 (UDP)
192.168.0.24:137 (UDP)
192.168.0.26:137 (UDP)
192.168.0.27:137 (UDP)
192.168.0.32:137 (UDP)
192.168.0.36:137 (UDP)
192.168.0.43:137 (UDP)
192.168.0.48:137 (UDP)
192.168.0.54:137 (UDP)
192.168.0.83:137 (UDP)
192.168.0.85:137 (UDP)
192.168.0.93:137 (UDP)
192.168.0.9:137 (UDP)
20.62.24.77:443 (TCP)
20.80.129.13:443 (TCP)
20.99.132.105:443 (TCP)
20.99.133.109:443 (TCP)
20.99.184.37:443 (TCP)
209.197.3.8:80 (TCP)
23.216.147.64:443 (TCP)
23.216.147.76:443 (TCP)
23.40.197.137:443 (TCP)
23.40.197.184:443 (TCP)
23.44.161.156:80 (TCP)
52.184.206.73:443 (TCP)
52.251.79.25:443 (TCP)
8.240.228.126:80 (TCP)
91.189.91.43:443 (TCP)
a83f:8110:0:0:0:0:1400:0:53 (UDP)
a83f:8110:0:0:100:0:1800:0:53 (UDP)
a83f:8110:0:0:10:0:0:0:53 (UDP)
a83f:8110:0:0:1400:0:0:0:53 (UDP)
a83f:8110:0:0:1400:1400:2800:3800:53 (UDP)
a83f:8110:0:0:1b00:100:2800:0:53 (UDP)
a83f:8110:0:0:2000:0:0:0:53 (UDP)
a83f:8110:0:0:2800:0:0:0:53 (UDP)
a83f:8110:0:0:4a82:21:0:0:53 (UDP)
a83f:8110:0:0:4d82:21:0:0:53 (UDP)
a83f:8110:0:0:5800:0:0:0:53 (UDP)
a83f:8110:0:0:5c00:0:60cf:15ba:53 (UDP)
a83f:8110:0:0:6782:21:0:0:53 (UDP)
a83f:8110:0:0:678c:21:0:0:53 (UDP)
a83f:8110:0:0:68d5:90ce:fd7f:0:53 (UDP)
a83f:8110:0:0:700:700:2800:4000:53 (UDP)
a83f:8110:0:0:702:0:0:0:53 (UDP)
a83f:8110:0:0:8a01:0:0:0:53 (UDP)
a83f:8110:0:0:9845:77a0:db01:0:53 (UDP)
a83f:8110:0:0:b00:b00:2800:1800:53 (UDP)
a83f:8110:0:0:d0ad:b403:0:0:53 (UDP)
a83f:8110:0:0:e0c0:1c74:8b81:ffff:53 (UDP)
a83f:8110:0:200:0:0:0:0:53 (UDP)
a83f:8110:0:5:5000:0:f141:10b8:53 (UDP)
a83f:8110:102:0:b0ff:ffff:4300:3a00:53 (UDP)
a83f:8110:106:0:0:5:5000:0:53 (UDP)
a83f:8110:1749:73ff:1749:73ff:1a4b:73ff:53 (UDP)
a83f:8110:1800:0:0:0:0:0:53 (UDP)
a83f:8110:2002:0:0:0:0:0:53 (UDP)
a83f:8110:205:dff:207:10ff:5:eff:53 (UDP)
a83f:8110:2600:0:7b38:3561:3632:6130:53 (UDP)
a83f:8110:2800:0:2800:0:1800:0:53 (UDP)
a83f:8110:2800:1800:4000:1800:1800:100:53 (UDP)
a83f:8110:2b57:80ff:2c58:81ff:2c57:82ff:53 (UDP)
a83f:8110:2c02:0:0:0:0:0:53 (UDP)
a83f:8110:2e74:6578:7424:7800:c01f:0:53 (UDP)
a83f:8110:30f7:7a22:a0ff:ffff:6e6b:2000:53 (UDP)
a83f:8110:4100:4300:5000:4900:5f00:4800:53 (UDP)
a83f:8110:4100:6c00:6c00:6f00:7700:2000:53 (UDP)
a83f:8110:4747:47ff:4747:47ff:4747:47ff:53 (UDP)
a83f:8110:50e:18ff:40d:17ff:20b:15ff:53 (UDP)
a83f:8110:684a:8d00:0:0:0:0:53 (UDP)
a83f:8110:6e00:4200:7500:6900:6c00:6400:53 (UDP)
a83f:8110:6f6f:6b75:7046:756e:6374:696f:53 (UDP)
a83f:8110:7565:41:6e79:76:616c:7565:53 (UDP)
a83f:8110:75e8:d701:7f21:6903:75e8:d701:53 (UDP)
a83f:8110:766b:500:a00:0:50f3:3100:53 (UDP)
a83f:8110:8063:3500:0:0:0:0:53 (UDP)
a83f:8110:80aa:88aa:90aa:98aa:a0aa:a8aa:53 (UDP)
a83f:8110:90a3:98a3:a0a3:a8a3:b0a3:b8a3:53 (UDP)
a83f:8110:9a02:0:8097:7fa3:9a02:0:53 (UDP)
a83f:8110:9e1f:e711:0:0:0:0:53 (UDP)
a83f:8110:a802:1300:100:0:0:0:53 (UDP)
a83f:8110:c352:d801:f86b:565:c352:d801:53 (UDP)
a83f:8110:c579:d801:beac:bf78:cce1:d301:53 (UDP)
a83f:8110:cdc6:d801:82c6:ca8a:cdc6:d801:53 (UDP)
a83f:8110:e0:ffff:e0:ffff:e0:ffff:53 (UDP)
a83f:8110:ffff:ffff:0:0:ffff:ffff:53 (UDP)
```

## Relations:

### `Lab01-01.exe` [[6]]

```
Contacted Domains: 31
Contacted IP Addresses: 45
```

# 7. What is the purpose of the files?

https://hybrid-analysis.com/sample/f50e42c8dfaab649bde0398867e930b86c2a599e8db83b8260393082268f2dba

https://hybrid-analysis.com/sample/58898bd42c5bd3bf9b1389f0eee5b39cd59180e8370eb9ea838a0b327bd6fe47