# Windows Command Line

Reference guide for essential Windows CMD commands — system info, networking, file management, and process control.

---

## Basic System Information

| Command | Description |
|---|---|
| `set` | Check your path from the command line |
| `ver` | Determine the operating system (OS) version |
| `systeminfo` | List various information about the system |
| `cls` | Clear the screen (equivalent to `clear` in Linux) |

---

## Networking Troubleshooting

| Command | Description |
|---|---|
| `ipconfig` | Check network information |
| `ipconfig /all` | Detailed network configuration |
| `ping target_name` | Check if you can reach a particular server |
| `tracert target_name` | Trace the route packets take to a destination |
| `nslookup host` | Look up a host or domain and return the IP address |

### `netstat` — Network Connections

`netstat` displays current network connections and listening ports.

| Flag | Description |
|---|---|
| `-a` | Displays all established connections and listening ports |
| `-b` | Shows the program associated with each connection |
| `-o` | Reveals the process ID (PID) associated with the connection |
| `-n` | Uses numerical form for addresses and port numbers |

---

## File and Disk Management

| Command | Description |
|---|---|
| `cd` | Display the current drive and directory |
| `dir` | List child directories (`dir /a` to display hidden files) |
| `tree` | Visually represent the directory tree |
| `mkdir` | Create a directory |
| `rmdir` | Remove a directory |
| `type` | Display text file contents |
| `copy` | Copy files or directories |
| `move` | Move files |
| `del` / `erase` | Delete a file |

### `more` — Paging Through Content

The `more` command can be used in two ways:

```batch
:: Display a text file page by page
more file.txt

:: Pipe long output from another command
some_command | more
```

---

## Task and Process Management

| Command | Description |
|---|---|
| `tasklist` | List all running processes |
| `taskkill /PID <id>` | Kill a process by its ID |
| `tasklist /?` | Display the help page |

### Filtering Processes

```batch
tasklist /FI "imagename eq sshd.exe"
```

This filters the task list to show only processes with the image name `sshd.exe`.
