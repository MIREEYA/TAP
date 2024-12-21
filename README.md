
# Minecraft Server Configuration

This repository contains the configuration for setting up a Minecraft server for practice purposes. The server provided is from the [Adventures in Minecraft GitHub](https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-Linux).

## Installation

### Clone the Repository

```bash
git clone https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-Linux.git
cd AdventuresInMinecraft-Linux
```

### Choose Your Operating System

There are different versions of the server setup depending on the operating system you are using:

- **Windows**: Use the `.bat` file
- **Linux**: Use the `.sh` file
- **Mac**: Use the `.command` file

## Project Structure

The project structure is as follows, regardless of the operating system:

```
AdventuresInMinecraft-Linux/
├── Server/
│   ├── start.bat       # For Windows
│   ├── start.sh        # For Linux
│   └── start.command   # For Mac
└── ...
```

## Starting the Server

To start the server, execute the appropriate `StartServer` file for your operating system:

- **Windows**: Double-click `start.bat`
- **Linux**: Run `./start.sh` in the terminal
- **Mac**: Double-click `start.command`

This will start the server with the default memory requirements (1024 MB).

## Modifying Memory Requirements

If the default memory of 1024 MB is not enough for your tasks, you can modify it directly in the `start.{bat|sh|command}` file located in the `/Server` directory. Open the file with a text editor and adjust the memory settings as needed.

---

## Folder agents
We have the code in a folder name agents. This folder is inside the folder "MyAdventures".
## asi??
