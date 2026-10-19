# Basic Networking for Data Engineers

Data engineering systems communicate over networks.

A Data Engineer may need to connect to:

- database servers
- APIs
- cloud virtual machines
- Airflow servers
- Spark clusters
- remote Linux machines

Understanding basic networking concepts helps me understand how these systems communicate.

---

# IP Address

An IP address identifies a device on a network.

Example:

```text
192.168.1.20
```

A simple mental model:

```text
IP address → where is the machine on the network?
```

In data engineering, a database or server may be located on another machine identified by an IP address.

---

# `hostname`

A hostname is the name of a machine.

Example:

```text
db-server
```

To see the current machine name:

```bash
hostname
```

To view IP addresses associated with the machine:

```bash
hostname -I
```

A simple distinction:

```text
hostname → machine name
IP       → network address
```

---

# Port

A port identifies a specific service running on a machine.

A useful mental model:

```text
IP   → building address
port → room inside the building
```

The same machine can run multiple services on different ports.

Common examples:

```text
22   → SSH
80   → HTTP
443  → HTTPS
5432 → PostgreSQL
```

Example:

```text
192.168.1.20:5432
```

means:

```text
192.168.1.20 → server address
5432         → service port
```

A common PostgreSQL connection may use:

```text
localhost:5432
```

Here:

```text
localhost → current machine
5432      → PostgreSQL port
```

---

# Viewing Listening Ports

I can inspect listening network ports with:

```bash
ss -tuln
```

Important information includes:

```text
Local Address:Port
```

This can help identify which services are listening on which ports.

---

# DNS

DNS means:

```text
Domain Name System
```

DNS translates human-readable names into IP addresses.

Example:

```text
github.com
```

is easier to remember than an IP address.

The basic process is:

```text
domain name
    ↓
DNS
    ↓
IP address
```

A useful mental model:

```text
name → number
domain → IP
```

---

# Looking Up Hosts

I tested DNS resolution using:

```bash
getent hosts github.com
```

and:

```bash
getent hosts google.com
```

This shows IP information associated with a hostname or domain.

---

# `curl`

`curl` can send requests to network services such as websites and APIs.

Example:

```bash
curl https://api.github.com
```

This sends an HTTP request to the GitHub API.

The response may contain JSON data.

Basic flow:

```text
terminal
   ↓
curl
   ↓
network
   ↓
API / website
   ↓
HTTP response
   ↓
terminal
```

---

# Why `curl` Matters in Data Engineering

Data Engineers often work with APIs.

`curl` can help answer questions such as:

```text
Is this API reachable?
Is this endpoint responding?
What data does it return?
What status code is returned?
```

It is useful for quick testing before writing application code.

---

# HTTP Headers

To request only HTTP headers:

```bash
curl -I https://github.com
```

The response may include a line such as:

```text
HTTP/2 200
```

The number is an HTTP status code.

---

# Common HTTP Status Codes

Important status codes include:

```text
200 → successful request

301 → permanent redirect
302 → temporary redirect

400 → bad request
401 → authentication required or failed
403 → forbidden
404 → not found

500 → server-side error
```

In data engineering, these can help diagnose API problems.

Example:

```text
200 → request succeeded
401 → authentication or API key problem
404 → endpoint may be wrong
500 → problem on the server side
```

---

# SSH

SSH means:

```text
Secure Shell
```

SSH allows me to securely connect from my terminal to another machine.

Basic syntax:

```bash
ssh username@server-address
```

Example:

```bash
ssh esma@192.168.1.50
```

Here:

```text
esma         → user on the remote machine
192.168.1.50 → remote machine IP
```

SSH commonly uses port:

```text
22
```

---

# Why SSH Matters

A Data Engineer may use SSH to connect to a remote Linux server.

After connecting, I can use normal Linux commands such as:

```bash
cd
ls
tail
grep
ps
top
```

For example:

```text
local computer
      ↓
     SSH
      ↓
remote Linux server
      ↓
inspect files, logs, and processes
```

---

# Checking the SSH Client

I can check whether SSH is installed with:

```bash
ssh -V
```

I can also find the executable with:

```bash
which ssh
```

Example:

```text
/usr/bin/ssh
```

---

# SSH Keys

SSH can authenticate using passwords or cryptographic keys.

A key pair contains:

```text
private key
public key
```

The basic idea is:

```text
my computer
    ↓
private key
    ↓
SSH authentication
    ↓
remote server
    ↓
public key
```

---

# Private Key

The private key must remain secret.

It should not be:

```text
shared in messages
committed to GitHub
uploaded publicly
given to other people
```

---

# Public Key

The public key can be shared.

It can be added to a remote server to allow key-based authentication.

---

# `ssh-keygen`

SSH key pairs can be created using:

```bash
ssh-keygen
```

I learned the concept, but I did not create a new key during this lesson because I did not need to connect to a remote server yet.

---

# Commands I Tested

```bash
hostname -I
hostname

ss -tuln

getent hosts github.com
getent hosts google.com

curl https://api.github.com

curl -I https://github.com

ssh -V
which ssh
```

---

# What I Learned

- an IP address identifies a machine on a network
- a hostname is a machine name
- a port identifies a service running on a machine
- different services can use different ports
- DNS converts domain names into IP addresses
- `getent hosts` can resolve hostnames
- `curl` can send HTTP requests
- APIs can return JSON responses
- HTTP status codes describe request results
- SSH allows secure remote access to Linux machines
- SSH commonly uses port 22
- SSH can use public/private key authentication
- private keys must remain secret

---

# Data Engineering Connection

Networking is part of normal data engineering work.

A Data Engineer may connect to:

```text
databases
APIs
remote servers
cloud virtual machines
distributed systems
pipeline services
```

A connection often involves:

```text
hostname or IP
        +
port
        +
authentication
```

Examples:

```text
database.company.com:5432
api.example.com:443
server.company.com:22
```

Understanding these concepts helps me debug questions such as:

```text
Is the server reachable?
Is the correct port open?
Can DNS resolve the hostname?
Is the API responding?
Is authentication working?
Can I connect to the remote machine?
```