<!-- end table of contents -->

<!-- /notes/linux-cli/md/linux-cli-body.md -->

<br>

`Last updated: Wed 30 Nov 2022 12:17 IST`

<br>

<!--<div style="page-break-before: always"></div>-->

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
echo *.log #print all .log files in dir
echo $USER #print logged in username
echo $HOME #print path to home directory
echo $HOSTNAME #print hostname
echo $SHELL #print shell
echo $BASH #print location of user bash
```

### man

### history

### which

<br>
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

<br>
<h1 id="directory-and-file-operations">Directory and file operations</h1>

### mkdir

```bash
mkdir test logs #two seperate dirs
mkdir -p test/logs #create by path, logs subdir (inside) of test dir
```

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

<br>
<h1 id="file-reading-and-manipulation">File reading and manipulation</h1>

### less

### more

```bash
more -2 file.txt
```

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
grep -r login /var/log/apache2 #recursive
grep -v login /var/log/apache2/access.log #select non-matching lines
grep -R #follow all symlinks
grep -l #print only names of FILEs with selected lines
grep -A 2 #print NUM lines of trailing context
grep -B 3 #print NUM lines of leading context
grep -A 2 -B 2 login /var/log/apache2/access.log #2 lines after, 2 before
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

<br>
<h1 id="archives-and-encryption">Archives and encryption</h1>

### tar

```bash
tar -czvf output.tar.gz input-dir/ #create gzip file verbose
tar -xvf file.tar.gz #extract file verbose
```

### zip

### unzip

```bash
unzip latest.zip
unzip file.zip -d /path/to/dir
```

### mcrypt

```bash
mcrypt backup.txt
rm backup.txt
mcrypt -d backup.txt.nc
```

<br>
<h1 id="users-and-groups">Users and groups</h1>

Related [linux-fs/important-sys-files](../linux-fs/important-sys-files.md)

### adduser

### useradd

```bash
useradd -m user1 #create the user's home directory
useradd -M user2 #do not create the user's home directory
```

### groupadd

### userdel

### groupdel

### usermod

```bash
usermod -a -G grpname username
usermod -aG sudo username #add user to sudo group
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

Related [linux-fs/important-sys-files](../linux-fs/important-sys-files.md)

### chmod

```bash
chmod +x file.sh #give execution permission
chmod 777 file.sh #give all permissions
```

### chown

```bash
chown userowner:usergrp file.sh #change file owner
```

### chgrp

```bash
chgrp staff /u #change the group of /u to "staff"
chgrp -hR staff /u  #change the group of /u and subfiles to "staff"
```

<br>
<h1 id="processes-and-system">Processes and system</h1>

### ps

```bash
ps -a #show processes for all users
ps -u #display process user/owner
ps -x #show processes not attached to a terminal
```

### free

```bash
free -h #free and used memory (RAM) in system human-readable
```

### top

### kill

```bash
kill 12345 #by process ID
kill -9 12345 #force kill by process ID
```

### systemctl

```bash
systemctl reboot #reboot machine
systemctl status sshd #status of ssh daemon service
systemctl stop sshd
systemctl start sshd
systemctl enable sshd
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
shutdown -h now #halt, time
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
mount /dev/sdb1 /media/usb
```

<br>
<h1 id="networking">Networking</h1>

### ping

### host

### wget

```bash
wget -O /dev/null http://speedtest.wdc01.softlayer.com/downloads/test100.zip #wget speed test
wget file.sh | sh #download shell script and run it
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
#### Setting up NIC to use DHCP

```bash
echo "iface eth0 inet dhcp" >> /etc/network/interfaces
ifconfig eth0 down
ifconfig eth0 up
```

#### Setting up NIC to use static IP

```bash
ifconfig eth0 down
```

`nano /etc/network/interfaces`

```bash
iface eth0 inet static
    address 192.168.44.33
    netmask 255.255.255.0
    gateway 192.168.44.2
ifconfig eth0 up
```

### ip

```bash
ip a
```

### dhclient

### iftop

### netstat

```bash
netstat -a #display all sockets (default: connected)
netstat -r #display IP routing table
netstat -i #display interface table
netstat -l #display listening server sockets, active internet connections
netstat -at #all tcp
netstat -au #all udp
netstat -p #show PID/name for socket
```

### ssh

```bash
ssh user@host
```

### scp

```bash
scp user@host:/home/user/file.txt destination/
```

### nc

See [cyber/exploitation#nc](../cyber/exploitation.md#nc)

```bash
nc -l -p 4444 #listen for inbound connections, local port
nc 10.8.22.123 4444 #tcp connection to ip and port
nc -lvp 7777 -e /bin/bash #listen, verbose, port, execute
```
<br>

[Back to top](#)