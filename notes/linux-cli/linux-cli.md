# Linux Command-line interface

**Table of Contents:**

- [Package management](#package-management)
- [Shell](#shell)
- [Files and filesystem navigation](#files-and-filesystem-navigation)
- [Text editing](#text-editing)
- [Users and groups](#users-and-groups)
- [Change permissions, ownership, and groups](#change-permissions-ownership-and-groups)
- [Processes and system](#processes-and-system)
- [Networking](#networking)

<br>

`Last updated: Wed 23 Nov 2022 20:03`

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

<div style="page-break-before: always"></div>

<h1 id="shell">Shell</h1>

### echo

```bash
echo -e "line1\nline2" #enable interpretation of backslash escapes
echo -n #do not output trailing newline
```

### man

### history

<div style="page-break-before: always"></div>

<h1 id="files-and-filesystem-navigation">Files and filesystem navigation</h1>

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

### wc

```bash
wc -c file.txt #byte count
wc -m file.txt #character count
wc -w file.txt #word count
wc -l file.txt #line count
```

### sort

```bash
sort -n nums.txt #ascending sort
sort -nr nums.txt #descending sort
sort -hr nums.txt #descending sort
```

### uniq

```bash
uniq -c nums.txt #unique lines
```

### file

### watch

<div style="page-break-before: always"></div>

<h1 id="text-editing">Text editing</h1>

### nano

<div style="page-break-before: always"></div>

<h1 id="users-and-groups">Users and groups</h1>


### adduser

### useradd

### userdel

### usermod

```bash
usermod -a -G grpname username
```

### sudo

### su

### id

### whoami

### passwd

<div style="page-break-before: always"></div>

<h1 id="change-permissions-ownership-and-groups">Change permissions, ownership, and groups</h1>

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

<div style="page-break-before: always"></div>

<h1 id="networking">Networking</h1>

### ping

### wget

### curl

```bash
curl -o file.tar.gz http://server/file2.tar.gz #Write to file instead of stdout
curl -u username:password ftp://server/
```

### traceroute

### ifconfig

### ip

### netstat

```bash
netstat -at #all tcp
netstat -au #all udp
netstat -p #show process
```

### nmap

### ssh

```bash
ssh user@host
```

### scp

```bash
scp user@host:/home/user/file.txt destination/
```