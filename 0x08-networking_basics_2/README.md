# Networking Basics #1

Welcome to the Networking Basics #1 project! In this project, you will explore various networking concepts and tasks related to network configuration on an Ubuntu system.

## Project Details

- **Project Weight**: 1
- **Start Date**: October 4, 2023, 6:00 AM
- **End Date**: October 6, 2023, 6:00 AM
- **Checker Release Date**: October 6, 2023, 6:00 AM
- **Auto Review**: An auto review will be launched at the deadline.

## Project Resources

Before you begin, make sure to read or watch the following resources:

- [What is localhost](#)
- [What is 0.0.0.0](#)
- [What is the hosts file](#)
- [Netcat examples](#)

You can also refer to the following manual pages for help:

- `ifconfig`
- `telnet`
- `nc` (Netcat)
- `cut`

## Learning Objectives

By the end of this project, you should be able to explain the following networking concepts without relying on external sources:

**General**
1. What is localhost/127.0.0.1?
2. What is 0.0.0.0?
3. What is /etc/hosts?
4. How to display your machine’s active network interfaces.

## Requirements

Please ensure that you meet the following requirements for this project:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- You must include a `README.md` file at the root of the project folder.
- All your Bash script files must be executable.
- Your Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any errors.
- The first line of all your Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

## Tasks

### Task 0: Change your home IP (Mandatory)

Write a Bash script that configures an Ubuntu server to meet the following requirements:

- `localhost` resolves to `127.0.0.2`.
- `facebook.com` resolves to `8.8.8.8`.

Example:
```bash
$ ping localhost
# PING localhost (127.0.0.1) ...

$ ping facebook.com
# PING facebook.com (157.240.11.35) ...

$ sudo ./0-change_your_home_IP
$ ping localhost
# PING localhost (127.0.0.2) ...

$ ping facebook.com
# PING facebook.com (8.8.8.8) ...

