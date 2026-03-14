# Windows PowerShell

PowerShell is a powerful tool from Microsoft designed for task automation and configuration management. It combines a command-line interface and a scripting language built on the .NET framework.

---

## Getting Started

PowerShell can be launched from a Command Prompt (`cmd.exe`) by typing `powershell` and pressing ++enter++.

PowerShell commands are known as **cmdlets**.

### Discovering Commands

| Cmdlet | Description |
|---|---|
| `Get-Command` | List all available cmdlets |
| `Get-Command -CommandType "Function"` | Filter commands based on type |
| `Get-Help` | Detailed information about cmdlets |
| `Get-Alias` | Lists all aliases available |

!!! tip
    Use `Get-Help <cmdlet> -Examples` to see practical usage examples for any command.

---

## Navigating the File System

| Cmdlet | Description |
|---|---|
| `Get-ChildItem` | Lists files and directories at a specified `-Path` |
| `Set-Location` | Navigate to a different directory |
| `New-Item` | Create a new item (specify path and type) |
| `Remove-Item` | Removes both directories and files |
| `Copy-Item` | Equivalent to `copy` |
| `Move-Item` | Equivalent to `move` |
| `Get-Content` | Read and display the contents of a file |

### Creating a New Directory

```powershell
New-Item -Path ".\Documents" -ItemType "Directory"
```

---

## System and Network Information

| Cmdlet | Description |
|---|---|
| `Get-ComputerInfo` | Retrieves comprehensive system information |
| `Get-LocalUser` | Lists all local user accounts on the system |
| `Get-NetIPConfiguration` | Provides detailed information about the network |
| `Get-NetIPAddress` | Shows details for all IP addresses configured |
| `Get-Process` | Detailed view of all currently running processes |
| `Get-Service` | Retrieval of information about service status |
| `Get-NetTCPConnection` | Displays current TCP connections |
| `Get-FileHash` | For generating file hashes |

### Generating a File Hash

```powershell
Get-FileHash -Path .\ship-flag.txt
```

---

## Remote Command Execution

`Invoke-Command` is essential for executing commands on remote systems.

!!! warning "Security Note"
    Remote command execution requires proper authentication and should only be used on systems you have authorization to access.

---

## Quick Reference

=== "File Operations"

    ```powershell
    # List files in current directory
    Get-ChildItem

    # Read a file
    Get-Content .\myfile.txt

    # Copy a file
    Copy-Item .\source.txt .\destination.txt

    # Create a new directory
    New-Item -Path ".\NewFolder" -ItemType "Directory"
    ```

=== "System Info"

    ```powershell
    # Get system details
    Get-ComputerInfo

    # List running processes
    Get-Process

    # Check services
    Get-Service

    # View network config
    Get-NetIPConfiguration
    ```

=== "Network"

    ```powershell
    # View IP addresses
    Get-NetIPAddress

    # View TCP connections
    Get-NetTCPConnection

    # Generate file hash
    Get-FileHash -Path .\file.txt
    ```
