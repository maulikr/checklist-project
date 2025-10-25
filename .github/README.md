# Remote Python Development with vsCode & Ubuntu Server

A step-by-step guide to set up VS Code on your desktop for remote Python development on an Ubuntu server (like Lenovo Tiny).

[[_TOC_]]

## Prerequisites

- VS Code on your desktop (Windows/macOS/Linux)
- SSH access to your Lenovo Tiny (Ubuntu Server)
- VS Code extensions:
   - Remote - SSH (by Microsoft)
   - Python (by Microsoft)

## Step-by-Step Setup

### Install and Configure SSH on Ubuntu Server

On your Ubuntu server:

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
```

Then check your server's IP address:

```bash
ip a
```

You'll get something like 192.168.1.42.

Test the connection from your desktop:

```bash
ssh user@192.168.1.42
```

### Install VS Code + Remote SSH Extension

In VS Code on your desktop:

1. Go to Extensions `(Ctrl+Shift+X)`
1. Search and install "**Remote - SSH**"
1. Press `F1` → type "**Remote-SSH: Connect to Host...**"
1. Add your server: `ssh user@192.168.1.42`

This will open a new VS Code window connected to your Ubuntu server.

### Install Python on Ubuntu Server

If not already installed:

```bash
sudo apt install python3 python3-venv python3-pip -y
```

Create a virtual environment for your project:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Python Extension on Remote Side

VS Code will automatically prompt to install the Python extension on the remote server.

After installation:

1. Open any Python Project
1. Press `Ctrl+Shift+P` → "**Python: Select Interpreter**"
1. Choose the Python environment on the remote server (`/usr/bin/python3` or `.venv/bin/python`)

### Done

- All Python code runs on the Ubuntu server
- VS Code on your desktop acts as a remote editor and debugger
- Your desktop stays light and clean (no local Python, packages, etc.)

## Advanced SSH Configuration

The `C:\Users\Administrator\.ssh\config` file is where VS Code looks for SSH connection settings.

### Example SSH Config Entry

Open the file and add:
```text
Host ubuntu-tiny
    HostName 192.168.1.42
    User your_username
    Port 22
    IdentityFile C:\Users\Administrator\.ssh\id_rsa
```

Then in VS Code:

1. Press `F1`
1. Choose "Remote-SSH: Connect to Host..."
1. Select `ubuntu-tiny` (or whatever name you used)

VS Code will then connect via SSH and install the VS Code server on your Ubuntu Tiny.

### Optional: SSH Key Setup (Recommended)

Generate an SSH key to avoid typing your password every time:

On your desktop:

```bash
ssh-keygen -t rsa -b 4096
```

Copy your public key to the server:
```bash
ssh-copy-id your_username@192.168.1.42
```
Or manually:
```bash
cat ~/.ssh/id_rsa.pub | ssh your_username@192.168.1.42 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

## You're Ready!

Now you can:

- Develop Python applications remotely
- Use VS Code's full feature set (debugging, intellisense, etc.)
- Keep your development environment separate from your desktop
- Leverage server resources for computation-intensive tasks