 Partition Sorter - Intelligent File Organizer
[![Linux Support](https://img.shields.io/badge/Linux-Supported-green.svg)](https://www.linux.org)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
**Partition Sorter** is a powerful terminal-based file organization tool that automatically sorts files into categorized folders based on their type. Perfect for cleaning up messy drives and organizing your data efficiently.

---
## 📋 Table of Contents
- [Description](#-description)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [Dependencies](#-dependencies)
- [⚠️ IMPORTANT WARNINGS](#️-important-warnings)

---

## 🎯 Description
**Partition Sorter** helps you maintain a clean and organized file system by automatically moving files into categorized folders. The application:
- Detects mounted partitions on your Linux system
- Allows manual or automatic partition selection
- Sorts files into 7 categories: Videos, Audio, Photos, Documents, Compressed files, Programming files, and Others
- Remembers your preferences using a local JSON database
- Features both automatic and manual sorting modes

---

## ✨ Features
- **Automatic Partition Detection** - Scans and lists all mounted partitions
- **Smart File Categorization** - Supports 100+ file formats across 7 categories
- **Two Sorting Modes**:
  - *Automatic* - Sort all selected partitions at once
  - *Manual* - Choose specific partitions to sort
- **Persistent Configuration** - Saves your partition preferences in `data.json`
- **Colorful Terminal UI** - Easy-to-read interface with color coding
- **No Root Required** - Runs with user permissions for safety

---

## 📁 File Categories

|Category|File Types|
|---|---|
|**Videos**|.mp4, .mkv, .avi, .mov, .wmv, .flv, .webm + 20+ more|
|**Audio**|.mp3, .wav, .flac, .aac, .ogg, .m4a + 20+ more|
|**Photos**|.jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .svg + 15+ more|
|**Documents**|.txt, .pdf, .doc, .docx, .xls, .xlsx, .ppt, .md + 25+ more|
|**Programming**|.py, .js, .java, .c, .cpp, .go, .rs, .html, .css + 60+ more|
|**Compressed**|.zip, .rar, .7z, .tar, .gz, .bz2, .xz + 30+ more|
|**Others**|Any file type not matching above categories|


---

## 📸 Screenshots

![[Pasted image 20260505232739.png]]
## 📦 Installation:


### 1. install colorama

Choose your operating system:
#### **Arch Linux**

```bash
sudo pacman -S python-colorama
```


#### **Debian/Ubuntu/Linux Mint**

```bash
sudo apt install python3-colorama
```

#### **Fedora**

```bash
sudo dnf install python3-colorama
```

#### **RHEL/CentOS**

```bash
sudo yum install python3-colorama
```

#### **openSUSE**

```bash
sudo zypper install python3-colorama
```

#### **Other Linux distros or if package not available**

```bash
# Using pip (user installation)
pip3 install --user colorama

# Or system-wide (not recommended)
sudo pip3 install colorama

# Or using pipx (recommended for user apps)
pipx install colorama
```

### 2. Shell Setup

The `pnsr` command should work immediately. If not, add this to your shell config:
#### **For Bash users** (~/.bashrc)

```bash
echo 'alias pnsr="pnsr"' >> ~/.bashrc
source ~/.bashrc
```

#### **For Zsh users** (~/.zshrc)

```bash
echo 'alias pnsr="pnsr"' >> ~/.zshrc
source ~/.zshrc
```

#### **For Fish users** (~/.config/fish/config.fish)

```bash
echo 'alias pnsr="pnsr"' >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish
```

## Usage

Simply type:

```bash
pnsr
```

---

## ⚠️ **IMPORTANT WARNINGS**

### 🚨 **DO NOT DELETE THE APPLICATION FILES**

**CRITICAL:** The `pnsr.py` file and `data.json` configuration file contain your partition settings and preferences.

**If you delete `pnsr.py`**, the application will stop working    
**If you delete `data.json`**, you will lose all saved partition configurations     
These files are the **MAIN APPLICATION FILES** - keep them safe!
        If you delete pnsr.py, the application will stop working

If you delete data.json, you will lose all saved partition configurations
These files are the MAIN APPLICATION FILES - keep them safe!
