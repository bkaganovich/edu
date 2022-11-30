<!-- /notes/cyber/reconnaissance.md -->

<br>

`Last updated: Wed 30 Nov 2022 12:17 IST`

<br>

<h1 id="reconnaissance-tools">Reconnaissance tools</h1>

### nmap

```bash
nmap -sn 10.8.22.0/24 #host discovery
nmap -sS -p 1234 10.8.22.0/24 #TCP SYN scan
nmap -sT -p 1234 10.8.22.0/24 #TCP connect scan test connection 3-way-handshake
nmap -sU --top-ports 100 10.8.22.0/24 #UDP scans
nmap -sS -sV 10.8.22.123 #SYN stealth scan, service and version detection
nmap -sS -O 10.8.22.123 #OS detection
nmap -sS -T4 -p 1-1024 10.8.22.123 #timing and performance
nmap -A 10.8.22.123 #OS and version detection, script scanning, traceroute
```

### masscan

```bash
masscan -p0-1024 --interface eth0 172.16.127.0/24
masscan -p -4000 --interface eth0 127.0.0.1
```

### whois

### theHarvester

```bash
theHarvester -d google.com -l 300 -b all #domain, limit, source
```

### recon-ng

```bash
help
marketplace info all
marketplace search all
marketplace install recon/domains-hosts/hackertarget
modules load recon/domains-hosts/hackertarget
info
options set SOURCE yahoo.com
run
show hosts
```

### sublist3r

```bash
sublist3r -d google.com #finds subdomains
```

### dig

### dirsearch

```bash
dirsearch -u google.com #directory search
```

### fping

```bash
fping -gaq 192.168.1.0/24 #ping connectivity test, use CIDR, show active, quiet mode
fping -gqs 192.168.1.0/24 #use CIDR, quiet mode, print final statistics
```

### netdiscover

```bash
netdiscover -i eth0 -r 192.168.1.0/24 #active/passive ARP reconnaissance tool
netdiscover -r 192.168.0.0/24 #scan capture arp packets, discover hosts by range
```