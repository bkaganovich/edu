# Linux Command-line interface

**Table of Contents**

- [Package management](#page=2)
- [Shell](#page=2)
- [Filesystem navigation](#page=3)
- [File reading and manipulation](#page=4)
- [Archives and encryption](#page=6)
- [Users and groups](#page=7)
- [Permissions, ownership, and groups](#page=7)
- [Processes and system](#page=8)
- [Networking](#page=10)
- [Reconnaissance tools](#page=11)

<br>

`Last updated: Wed 26 Nov 2022 22:05`

<br>

<div style="page-break-before: always"></div>

<h1 id="package-management">Package management</h1>

_Debian_

### apt

```bash
apt install packagename
apt remove packagename
apt purge packagename
apt update
apt upgrade
```

### dpkg

```bash
dpkg -i package.deb
```

_Red Hat (RHEL, CentOS, Fedora)_

### dnf

```bash
dnf install packagename
dnf remove packagename
dnf update
```

### rpm

```bash
rpm -i package.rpm
```

_Arch_

### pacman

```bash
pacman -S packagename
pacman -Syu
```

<br>

<h1 id="shell">Shell</h1>

### echo

```bash
echo -e "line1\nline2" #enable interpretation of backslash escapes
echo -n #do not output trailing newline
```

### man

### history

<div style="page-break-before: always"></div>

<h1 id="filesystem-navigation">Filesystem navigation</h1>

### pwd

### ls

```bash
ls -R #recursive list
ls -r #reverse order while sorting
ls -S #sort by size
ls -shal #print size, human-readable, all, long listing format
```

### tree

```bash
tree -a -L 1 #tree 1 level all files, says "x directories, y files"
```

### cd

### mkdir

### rmdir

### touch

```bash
touch newfile.txt #creates newfile.txt
touch newfile.txt #if newfile.txt exists: updates time, no overwrite
```

### nano

### rm

```bash
rm -r directory/ #recursive dir removal
```

### cp

```bash
cp -R mydir/ destination/ #recursive dir copy
cp -v file.txt destination/ #verbose
```

### mv

<div style="page-break-before: always"></div>

<h1 id="file-reading-and-manipulation">File reading and manipulation</h1>

### less

### more

### tail

```bash
tail -n 3 file.txt #last 3 lines
```

### head

```bash
head -n 20 file.txt #first 20 lines
head -c 5k file.txt #first 5k bytes in size
```

### cat

```bash
cat -n file.txt #show line numbers
```

### grep

```bash
grep -r #recursive
grep -v #select non-matching lines
grep -R #follow all symlinks
grep -l #print only names of FILEs with selected lines
grep -A 2 #print NUM lines of trailing context
grep -B 3 #print NUM lines of leading context
```

### cut

```bash
cut -b 5 file.txt #get first 5 bytes in each line
cut -c 2,5,7 file.txt #get chars at 2nd, 5th, 7th place in each line
```

### sort

```bash
sort -n nums.txt #ascending sort
sort -nr nums.txt #descending sort
sort -hr nums.txt #descending sort
sort -nu #numeric unique sort
```

### uniq

```bash
uniq -c nums.txt #unique lines count, requires sorted list
```

### watch

### find

```bash
find / -name myfile.txt
```

### file

### stat

### wc

```bash
wc -c file.txt #byte count
wc -m file.txt #character count
wc -w file.txt #word count
wc -l file.txt #line count
```

<div style="page-break-before: always"></div>

<h1 id="archives-and-encryption">Archives and encryption</h1>

### tar

```bash
tar -czvf output.tar.gz input-dir/ #create gzip file verbose
tar -xvf file.tar.gz #extract file verbose
```

### zip

### unzip

### mcrypt

```bash
mcrypt backup.txt
rm backup.txt
mcrypt -d backup.txt.nc
```

<div style="page-break-before: always"></div>

<h1 id="users-and-groups">Users and groups</h1>

### adduser

### useradd

### groupadd

### userdel

### groupdel

### usermod

```bash
usermod -a -G grpname username
```

### sudo

### su

### id

### whoami

### who

### w

### last

### passwd

<br>
<h1 id="permissions-ownership-and-groups">Permissions, ownership, and groups</h1>

### chmod

```bash
chmod +x file.sh #give execution permission
chmod 777 file.sh #give all permissions
```

### chown

```bash
chown userowner:usergrp file.sh
```

### chgrp

```bash
chgrp staff /u #Change the group of /u to "staff"
chgrp -hR staff /u  #Change the group of /u and subfiles to "staff"
```

<div style="page-break-before: always"></div>

<h1 id="processes-and-system">Processes and system</h1>

### ps

```bash
ps -a
ps -u #display process user/owner
ps -x #processes not attached to terminal
```

### free

```
bash
free -h #free and used memory (RAM) in system human-readable
```

### top

### kill

```bash
kill pid
kill -9 pid #force kill
```

### systemctl

```bash
systemctl status sshd #status of ssh daemon service
systemctl stop sshd
systemctl start sshd
systemctl enable sshd
systemctl reboot
```

### service

```bash
service sshd status #status of ssh daemon service
service sshd stop
service sshd start
service sshd restart
```

### reboot

### shutdown

```bash
shutdown -h now #halt
```

### date

### uptime

### uname

```bash
uname -a
```

### hostname

### locale

### dmesg

### df

```bash
df -h #file system space usage human-readable
```

### fdisk

```bash
fdisk -l
fdisk /dev/sdb
```

### mkfs

```bash
mkfs.ext4 /dev/sdb1
```

### lsblk

### mount

```bash
mount /dev/sdb1/ /media/usb
```

<div style="page-break-before: always"></div>

<h1 id="networking">Networking</h1>

### ping

### host

### wget

```bash
wget -O /dev/null http://speedtest.wdc01.softlayer.com/downloads/test100.zip #wget speed test
wget file.sh | run #download sh and run it
```

### curl

```bash
curl -o file.tar.gz http://server/file2.tar.gz #Write to file instead of stdout
curl -u username:password ftp://server/
```

### traceroute

### ifconfig

```bash
ifconfig eth0
ifconfig eth0 up
ifconfig eth0 down
```

### ip

```bash
ip a
```

### dhclient

### iftop

### netstat

```bash
netstat -at #all tcp
netstat -au #all udp
netstat -p #show process
```

### ssh

```bash
ssh user@host
```

### scp

```bash
scp user@host:/home/user/file.txt destination/
```

<div style="page-break-before: always"></div>

<h1 id="reconnaissance-tools">Reconnaissance tools</h1>

### nmap

### whois

### theHarvester

```bash
theHarvester -d google.com -l 300 -b all #domain, limit, source
```

### recon-ng

```bash
recon-ng
> help
> marketplace info all
> marketplace search all
> marketplace install recon/domains-hosts/hackertarget
> modules load recon/domains-hosts/hackertarget
> info
> options set SOURCE yahoo.com
> run
> show hosts
```