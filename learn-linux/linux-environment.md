# Linux Environment

## Why Am I Learning Linux?

Linux is widely used in servers, cloud environments, containers, and data infrastructure.

Many tools used in data engineering run on Linux-based systems. Learning Linux helps me understand the environment where data pipelines and data platforms actually run.

My goal is not to memorize Linux commands. I want to understand how to work with files, processes, programs, services, and automation in a Linux environment.


## Linux

Linux is the kernel at the core of many operating systems.

The kernel is the part of an operating system that manages system resources such as:

- CPU
- memory
- storage
- devices
- processes
- networking

Linux-based operating systems combine the Linux kernel with other software and tools.


## Ubuntu

Ubuntu is a Linux distribution.

A Linux distribution combines the Linux kernel with system utilities, package managers, libraries, applications, and other software to provide a complete operating system environment.

Ubuntu is widely used for development, servers, cloud computing, and technical workloads.


## WSL

WSL stands for Windows Subsystem for Linux.

It allows a Linux environment to run inside Windows without requiring a traditional separate Linux installation.

In my current setup, I use Ubuntu through WSL as my Linux learning and development environment.


## Terminal, Shell and Bash

A terminal is the interface where I type commands and view their output.

A shell is a program that reads and interprets commands and starts the programs needed to execute them.

Bash is one of the most widely used shells in Linux and Unix-like environments.

A simple mental model is:

User → Terminal → Shell → Programs → Operating System


## Commands I Tested

```bash
pwd
whoami
ls
cd
mkdir
touch
code .