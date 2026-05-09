# 🐧 Linux CLI — Linux Terminal Simulator for Windows

A Python-based **Linux terminal emulator** that brings the Linux command-line experience to Windows users. Run familiar Linux commands directly from a beautifully styled, color-coded terminal prompt — no dual boot or WSL required.

---

## ✨ Features

- 🎨 **Colored terminal prompt** — mimics a real Linux shell (`username@Linux-Terminal:~`)
- 📁 **Dynamic path display** — current directory updates in the prompt in real time
- ⌨️ **15+ Linux commands** — covers navigation, file management, text utilities, and more
- 🛡️ **Error handling** — meaningful error messages for missing files, wrong usage, etc.
- 🧪 **Test suite** — included `test_cmd.py` for validating command behavior

---

## 📂 Project Structure

```
Linux_CLI/
├── app.py          # Entry point — starts the terminal session
├── check_cmd.py    # Command router — validates and dispatches commands
├── run_cmd.py      # Command implementations (all 15+ commands live here)
├── utils.py        # Utility functions (colored output helpers)
├── test_cmd.py     # Unit tests for commands
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Works on **Windows**, Linux, and macOS

### Installation

```bash
# Clone the repository
git clone https://github.com/LochanJangid/Linux_CLI.git

# Navigate into the project folder
cd Linux_CLI
```

### Running the Terminal

```bash
python app.py
```

You'll be greeted with a welcome banner and prompted for a username:

```
------------------------------------------------------------
-Welcome to Linux CLI
a linux terminal simulator for window users.

To see available commands, type "help" and press enter

------------------------------------------------------------

Username: lochan
lochan@Linux-Terminal:~$
```

---

## 🛠️ Available Commands

Type `help` in the terminal to list all available commands.

| Command | Syntax | Description |
|---------|--------|-------------|
| `pwd` | `pwd` | Print the current working directory |
| `cd` | `cd <dir>` / `cd ..` | Change directory |
| `ls` | `ls` | List files and folders (directories shown in blue) |
| `mkdir` | `mkdir <dir> [dir2 ...]` | Create one or more directories |
| `rmdir` | `rmdir <dir> [dir2 ...]` | Remove empty directories |
| `touch` | `touch <file> [file2 ...]` | Create one or more empty files |
| `cat` | `cat <file> [file2 ...]` | Display file contents |
| `rm` | `rm [-r] [-v] [-rv] <file>` | Remove files or directories recursively |
| `cp` | `cp <source> <dest>` | Copy a file |
| `mv` | `mv <source> <dest>` | Move/rename a file |
| `echo` | `echo "text"` / `echo "text" > file` | Print text or write to a file |
| `sort` | `sort <file>` | Sort lines of a file alphabetically |
| `join` | `join <file1> <file2> [> output]` | Join lines of two files side by side |
| `date` | `date` | Display the current date and time |
| `exit` | `exit` | Quit the terminal |

---

## 💻 Usage Examples

```bash
# Navigate directories
lochan@Linux-Terminal:~$ cd projects
lochan@Linux-Terminal:~/projects$ pwd
Thats me /home/lochan/projects

# File management
lochan@Linux-Terminal:~$ mkdir notes
lochan@Linux-Terminal:~$ touch notes/todo.txt
lochan@Linux-Terminal:~$ echo "Buy groceries" > notes/todo.txt
lochan@Linux-Terminal:~$ cat notes/todo.txt
Buy groceries

# List directory contents
lochan@Linux-Terminal:~$ ls
notes  app.py  run_cmd.py

# Copy and move files
lochan@Linux-Terminal:~$ cp notes/todo.txt notes/backup.txt
lochan@Linux-Terminal:~$ mv notes/backup.txt archive.txt

# Remove with verbose flag
lochan@Linux-Terminal:~$ rm -v archive.txt
removed "archive.txt"

# Recursive delete
lochan@Linux-Terminal:~$ rm -r notes

# Sort a file's content
lochan@Linux-Terminal:~$ sort words.txt

# Join two files line by line
lochan@Linux-Terminal:~$ join names.txt scores.txt > result.txt

# Check current date/time
lochan@Linux-Terminal:~$ date
Sat May 09 14:32:00 IST 2026

# Exit the terminal
lochan@Linux-Terminal:~$ exit
```

---

## 🧪 Running Tests

```bash
python test_cmd.py
```

The test suite validates the core command functions defined in `run_cmd.py`.

---

## 🏗️ How It Works

```
app.py  ──► Reads user input with a styled prompt
   │
   ▼
check_cmd.py  ──► Validates the command exists in the allowed list
   │                 Returns "command not found" for unknown input
   ▼
run_cmd.py  ──► Executes the matching function (e.g., ls(), mkdir(), rm())
   │
   ▼
utils.py  ──► Handles colored terminal output
```

Each command in `run_cmd.py` is a standalone Python function matched by name using `getattr`, making it easy to extend the project with new commands.

---

## 🔧 Adding New Commands

1. Add the function to `run_cmd.py`:
   ```python
   def mycommand(commands):
       # your implementation
       print("Hello from mycommand!")
   ```

2. Register it in `check_cmd.py`:
   ```python
   available_commands = [..., 'mycommand']
   ```

That's it — the dispatcher handles the rest automatically.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to add new commands, fix bugs, or improve documentation.

---

## 📄 License

This project is open source. See the repository for details.

---

## 👤 Author

**Lochan Jangid** — [@LochanJangid](https://github.com/LochanJangid)
