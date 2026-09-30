# Partition Sorter

**Intelligent file organizer for Linux**

Partition Sorter is a terminal-based file organization tool that sorts the files in
your drives and partitions into categorized folders based on their type. It is built
for cleaning up a messy download folder, a media drive, or a partition full of
unsorted files.

```
pnsr
```

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [File Categories](#file-categories)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Screenshots](#screenshots)
- [License](#license)

---

## Description

Partition Sorter walks the top level of a partition (or any folder you add as a
"partition") and moves each file into a subfolder based on its extension:

- Detects mounted partitions automatically via `lsblk`
- Lets you register extra folders as partitions
- Sorts into 7 categories, covering 230 file extensions
- Sorts one partition or all of them at once
- Never overwrites an existing file — collisions are renamed instead
- Remembers your configuration between runs

Folders are created on demand inside the target partition:

```
/mnt/data
├── Files
│   ├── Photos
│   ├── Videos
│   ├── Audio
│   ├── Documents
│   ├── Programming
│   ├── Compressed
│   └── Others
└── your_unsorted_files_here...
```

## Features

- **Automatic partition detection** — scans mounted partitions with `lsblk` and lists them
- **Smart categorization** — 230 extensions across 7 categories
- **Two sorting modes**
  - *Automatic* — sorts every partition you have enabled
  - *Manual* — pick a specific partition to sort
- **Collision-safe renaming** — if the destination already has a file with the same
  name, the incoming file is renamed `name (1).jpg`, `name (2).jpg`, and so on.
  Existing files are never overwritten or deleted.
- **Persistent configuration** — your partitions and auto-sort flags are saved
- **Colorful terminal UI** — color-coded menus and status output

## File Categories

| Category | Recognized examples | Count |
| --- | --- | --- |
| Videos | `.mp4` `.mkv` `.avi` `.mov` `.wmv` `.flv` `.webm` `.m4v` `.mpeg` `.ts` + 15 more | 25 |
| Audio | `.mp3` `.wav` `.flac` `.aac` `.ogg` `.m4a` `.opus` `.wma` + 17 more | 25 |
| Photos | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.tiff` `.webp` `.svg` `.heic` `.raw` + 19 more | 29 |
| Documents | `.txt` `.pdf` `.doc` `.docx` `.xls` `.xlsx` `.ppt` `.md` `.csv` `.epub` + 24 more | 34 |
| Programming | `.py` `.js` `.ts` `.java` `.c` `.cpp` `.go` `.rs` `.rb` `.php` + 70 more | 80 |
| Compressed | `.zip` `.rar` `.7z` `.tar` `.gz` `.bz2` `.xz` `.zst` `.exe` `.iso` + 29 more | 39 |
| Others | anything that does not match the above | — |

Categories are checked in the order above, so a file that matches more than one
category lands in the first match. For example `.jar` is both compressed and
programming, and is sorted into **Programming**.

## Requirements

- **Linux** (partition detection relies on `lsblk`)
- **Python 3.10 or newer** — the app uses a `match`/`case` statement
- **colorama**

Check your Python version:

```bash
python3 --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/itsawouki/Partition-Sorter.git
cd Partition-Sorter
```

### 2. Install colorama

Choose the command for your distribution:

```bash
# Arch Linux
sudo pacman -S python-colorama

# Debian / Ubuntu / Linux Mint
sudo apt install python3-colorama

# Fedora
sudo dnf install python3-colorama

# RHEL / CentOS
sudo yum install python3-colorama

# openSUSE
sudo zypper install python3-colorama
```

If your distribution has no package, or you prefer pip:

```bash
# user install (recommended)
pip3 install --user colorama

# or system-wide (not recommended)
sudo pip3 install colorama
```

### 3. Create the `pnsr` command

This installs a launcher into `~/.local/bin`, so no root access is required. Run it
from inside the cloned repository:

```bash
mkdir -p ~/.local/bin
printf '#!/bin/sh\nexec python3 %s/pnsr.py "$@"\n' "$PWD" > ~/.local/bin/pnsr
chmod +x ~/.local/bin/pnsr
```

The launcher stores the absolute path to your clone, so it keeps working from any
directory.

Make sure `~/.local/bin` is on your `PATH`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc   # or ~/.zshrc
source ~/.bashrc
```

Verify it works:

```bash
which pnsr
pnsr
```

### Updating

```bash
cd /path/to/Partition-Sorter
git pull
```

The launcher points at your clone, so a `git pull` is all you need — no reinstall.

## Usage

Run:

```bash
pnsr
```

The main menu:

```
1: Show partitions       list the partitions the app knows about
2: Detect partitions     scan for mounted partitions and add them
3: Manual partitioning   register a mounted path by hand
4: Sort Files            sort a partition
5: Settings              manage auto-sort flags, folders, and partitions
6: Quit
```

A typical first run:

1. **2 — Detect partitions** to add your mounted partitions.
2. **5 — Settings → 2** to add a plain folder (such as `~/Downloads`) as a partition.
3. **4 — Sort Files → 2**, then pick the partition number you want.

Then in **Settings → 1** you can enable *auto-sort* for a partition, which means
option **4 → 1 (Automatic)** will sort it along with the others.

## Configuration

Your configuration is stored in a file called **`data.json`**, which is created
automatically on first run.

> [!IMPORTANT]
> `data.json` is created in the **current working directory**, not next to the
> script. If you run `pnsr` from different folders, each folder gets its own
> separate configuration. Pick one directory to run it from, or add a `cd` to your
> launcher.

Do not delete `data.json` — it holds your partition list and auto-sort flags. It is
machine-specific, so it should not be committed to version control.

## Screenshots

{image.png}

## License

<!-- TODO: add your license, e.g. MIT. -->
_License not yet specified._

## Disclaimer

Partition Sorter moves files. Make a backup of anything important before running it
on a partition for the first time. The app does not delete files, but a file moved
into the wrong category is still a file you have to find again.
