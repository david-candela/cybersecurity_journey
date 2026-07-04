# Snapped Phi-shing Line

| | |
|---|---|
| **Date Completed** | 27/01/2025 |
| **Difficulty** | <span class="diff-tag">Easy</span> |
| **Room Link** | [tryhackme.com/room/snappedphishingline](https://tryhackme.com/room/snappedphishingline) |

---

## :clipboard: Overview

Premium room! Challenge room!

In a Linux environment we encounter some reported phishing emails that we have to analyze. Apply learned skills to probe malicious emails and URLs, exposing a vast phishing campaign.

---

## :dart: Key Learning Objectives

- [x] Analysing the email samples provided
- [x] Retrieving the phishing kit used by the adversary
- [x] Using CTI-related tooling to gather more information about the adversary

---

## :pencil: Notes

### Task 1: Identify All Phishing Emails

I located all phishing emails on a file in the desktop.

### Task 2: Read and First Analysis of the Emails

I opened all of the emails using Thunderbird client, read them, saw all the attachments, located the adversary's email and used CyberChef to defang the address.

### Task 3: Defang URL

The phishing page was inside an `.html` file. I opened the file with TextEdit and used CyberChef to defang the URL.

### Task 4: Locate the .zip

I noticed that the phishing URL sent to the victims contained a parent directory as `hxxp[://]kennaroads[.]buzz/data/`. There I found the phishing kit in a `.zip` format.

### Task 5: Checksum for the File

I used the command `sha256sum` to find the SHA256 of the `.zip` file.

```bash
sha256sum phishing-kit.zip
```

### Task 6: Analyze the SHA256

I went to VirusTotal and pasted the hash of the file to see other reports. It's reported as a trojan.

!!! warning "VirusTotal Tip"
    Always check VirusTotal for known hashes before opening unknown files. It aggregates results from dozens of antivirus engines.

### Task 7: Analyze the Adversary's Directory

I found a file containing a log with all email and passwords stored.

### Task 8: Find the Email the Adversary Uses to Receive Stolen Credentials

I had to unzip the file using the `unzip` command. Then I used `grep` to find any email addresses inside all the files in the folder:

```bash
unzip phishing-kit.zip
grep -r "@.*\.com" .
```

`-r` performs a recursive search through all the files.

### Final Task: Find the Flag

!!! tip "Hint"
    The hint says there's a file named `flag.txt`.

Inside the adversary website there's a directory named `office365` which we cannot enter. If we guess that `flag.txt` is inside, we can access it directly — it reveals a base64-encoded string. Upon decoding, the code is in reverse.

---

## :wrench: Tools Used

| Tool | Purpose |
|---|---|
| [CyberChef](https://gchq.github.io/CyberChef/) | Defanging URLs and email addresses, base64 decoding |
| Linux Terminal | File navigation, `sha256sum`, `grep`, `unzip` |
| [VirusTotal](https://www.virustotal.com) | Hash analysis and threat intelligence |
| Thunderbird | Inspecting `.eml` email files and attachments |

---

## :bulb: Key Takeaways

1. Gather and use all previously known tools in a real live environment
2. Analyze each and every layer of the phishing email
3. Use Linux's terminal to automate searches
