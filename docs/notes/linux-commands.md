# Linux Commands

A reference guide for Linux commands: file navigation, process management, user administration, and networking.

---

## Getting Help

| Command | Description |
|---|---|
| `man <command>` | Open the manual page for a command |
| `whatis <command>` | Display a one line description of a command |
| `apropos <keyword>` | Search manual pages for a keyword |
| `<command> --help` | Quick help for a command |

```bash
# Examples
man usermod           # full manual for usermod
whatis nano           # quick description of nano
apropos -a change password  # search for commands related to changing passwords
```

---

## Listing and Navigating

| Command | Description |
|---|---|
| `ls` | List directory contents |
| `ls -l` | Long format, shows permissions, owner, size, date |
| `ls -a` | Show all files including hidden |
| `ls -la` | Long format + hidden files |
| `pwd` | Print working directory |
| `cd <dir>` | Change directory |
| `cd ..` | Go to parent directory |
| `cd ~` | Go to home directory |

!!! tip
    Type `cd ../D` and press ++tab++ to autocomplete directories starting with "D".

---

## File and Directory Management

| Command | Description |
|---|---|
| `mkdir <name>` | Create a directory |
| `mkdir 'my cool file'` | Create a directory with spaces in the name |
| `rmdir <dir>` | Remove an empty directory |
| `touch <file>` | Create an empty file |
| `rm <file>` | Remove a file |
| `cp <src> <dest>` | Copy a file |
| `cp -r <src> <dest>` | Copy a directory recursively |
| `mv <src> <dest>` | Move or rename a file |

```bash
cp *.png ~/Desktop    # copy all PNGs to the Desktop
```

---

## Viewing File Contents

| Command | Description |
|---|---|
| `cat <file>` | Display entire file contents (concatenate) |
| `less <file>` | Browse a file interactively |
| `head <file>` | Show the first 10 lines |
| `tail <file>` | Show the last 10 lines |

### Navigating in `less`

| Key | Action |
|---|---|
| Arrow keys | Scroll up/down |
| `g` | Go to start of file |
| `G` | Go to end of file |
| `/<word>` | Search for a word |
| `q` | Quit |

---

## Searching

| Command | Description |
|---|---|
| `grep <pattern> <file>` | Search for a pattern in a file |
| `find <path> -name <pattern>` | Search for files by name |

```bash
# Search for files containing "log" in the projects directory
find /home/analyst/projects -name "*log*"
# * is a wildcard representing unknown characters
```

---

## Input, Output, and Piping

| Operator | Description |
|---|---|
| `echo <text>` | Print text to stdout |
| `>` | Redirect output to a file (overwrites) |
| `>>` | Redirect output to a file (appends) |
| `2>` | Redirect error messages (stderr) |
| `/dev/null` | Discard output (the "dark void") |
| `\|` | Pipe, send output of one command as input to another |

```bash
echo "hello" > output.txt       # write to file
echo "more" >> output.txt       # append to file
ps -ef | grep Chrome            # pipe process list into grep
```

!!! info "Piping"
    The `|` symbol sends the output of the command on the left as input to the command on the right.
---

## Users and Groups

### User Management

| Command | Description |
|---|---|
| `sudo` | Run a command as superuser |
| `su` | Switch user (`sudo su -` for root) |
| `exit` | Logout from current user |
| `passwd` | Change password (stored in `/etc/shadow`) |
| `sudo passwd -e <user>` | Expire a user's password (force reset) |
| `sudo useradd <user>` | Create a new user |
| `userdel <user>` | Delete a user (keeps their files) |
| `userdel -r <user>` | Delete a user and all their home directory files |

### Group Management with `usermod`

| Command | Description |
|---|---|
| `usermod -g <group> <user>` | Change a user's primary group |
| `usermod -a -G <group> <user>` | Add user to a group without replacing existing groups |
| `usermod -d <dir> <user>` | Change user's home directory |
| `usermod -l <newname> <user>` | Change user's login name |
| `usermod -L <user>` | Lock the account |

```bash
useradd -G finance,admin david     # create user in multiple groups
usermod -a -G finance david        # add david to finance without removing other groups
```

### Permissions and Ownership

| Command | Description |
|---|---|
| `ls -l <path>` | View permissions and ownership |
| `chmod <perms> <file>` | Change file permissions |
| `chown <user> <file>` | Change file owner |
| `chown :<group> <file>` | Change file group (note the `:` prefix) |

#### Permission Values

| Value | Permission |
|---|---|
| `r` = 4 | Read |
| `w` = 2 | Write |
| `x` = 1 | Execute |
| `rwx` = 7 | Full permissions |

```bash
chmod u+x my_cool_file               # give owner execute permission
sudo chown david access.txt           # david is now the owner
sudo chown :security access.txt       # the "security" group is now the group owner
```

---

## Package Management

=== "APT (Debian/Ubuntu)"

    | Command | Description |
    |---|---|
    | `sudo apt install <pkg>` | Install a package |
    | `sudo apt remove <pkg>` | Remove a package |
    | `apt update` | Update package lists |
    | `apt upgrade` | Upgrade installed packages |
    | `sudo apt full-upgrade` | Upgrade including kernel if possible |

=== "dpkg"

    | Command | Description |
    |---|---|
    | `sudo dpkg -i <file>.deb` | Install a `.deb` package |
    | `sudo dpkg -r <pkg>` | Remove a package |
    | `dpkg -l` | List installed packages |
    | `dpkg -l \| grep <name>` | Search for a specific package |

=== "Other"

    ```bash
    uname -r                  # check kernel version
    7zip e my_file.tar        # extract an archive
    ```

---

## Processes

| Command | Description |
|---|---|
| `ps` | List running processes |
| `ps -x` | List all processes for the current user |
| `ps -ef` | All processes with full details |
| `top` | Live view of most CPU-heavy processes |
| `uptime` | System uptime, number of users |
| `lsof` | List open files and which processes use them |

### Managing Processes

| Command | Description |
|---|---|
| ++ctrl+c++ | Interrupt a running process |
| `kill <PID>` | Terminate a process gracefully |
| `kill -KILL <PID>` | Force kill without waiting for cleanup |
| `kill -TSTP <PID>` | Suspend a process |
| `kill -CONT <PID>` | Resume a suspended process |

```bash
ps -ef | grep Chrome     # find Chrome's PID
kill 12345               # then kill it
```

---

## Disk Management

| Command | Description |
|---|---|
| `parted -l` | List disk partitions |
| `mkpart` | Create a partition |
| `mkfs -t ext4` | Format a partition as ext4 |
| `mount` | Mount a filesystem |
| `umount` | Unmount a filesystem |
| `mkswap` | Create swap space |

```bash
mkpart primary ext4 1MiB 5GiB    # create a 5GB ext4 partition
```

---

## Networking and Remote Access

| Command | Description |
|---|---|
| `ifconfig` | Configure / display network interfaces |
| `scp <src> <dest>` | Copy files between computers securely |
| `dig <domain>` | Query DNS name servers |

```bash
# Serve files from current directory over HTTP
python -m http.server 8080
```

---

## Services

| Command | Description |
|---|---|
| `service <name> status` | Check a service's status |
| `service <name> reload` | Reload config without stopping the service |
| `systemctl enable <name>` | Enable a service on boot |
| `systemctl disable <name>` | Disable a service on boot |

```bash
sudo vim /etc/vsftpd.conf    # edit a service config file
```

---

## Imaging

| Command | Description |
|---|---|
| `dd` | Copy input to output (used for disk imaging) |

!!! warning
    `dd` is powerful but dangerous — double-check your `if=` (input) and `of=` (output) parameters before running.
