# CodeAlpha_Task-Basic-Network-Sniffer

*COMPANY* : CODEALPHA

*NAME* : PRIYA BABARE

*INTERN ID* : CA/MA1/7455

*DOMAIN* : CYBER  SECURITY 

*DURATION* : 4 WEEKS

# Project Overview

This project is a Basic Network Sniffer created using Python and the Scapy library. It was built as part of my cybersecurity internship to demonstrate the ability to monitor and analyze live network traffic. Through this tool, I gained practical knowledge of how data flows in a network and how packets are structured, which is crucial for roles like Cyber Threat Intelligence Analyst or Network Security Professional.

# Objective

- The main aim of this project is to:

- Understand how network packets are structured.

- Learn how to capture and analyze real-time data packets.

- Create a tool that monitors IP traffic and identifies TCP packets with port numbers.

- Strengthen core networking and Python skills relevant to cybersecurity.

# What I Learned

- Basics of packet sniffing using Scapy.

- Difference between IP, TCP, and other protocols.

- How to inspect live data flow across a network interface.

- Importance of analyzing ports and packet types in cybersecurity.

# Tools and Technologies

- Python 3 (**Core programming language**).        

- Scapy (**Capturing and analyzing packets**).

- Ubuntu (WSL) (**Running the Python sniffer safely**).

- VS Code (**Writing and editing the code**).    

#  How It Works 
**1. Listening to the Network:**

- The program uses a tool called Scapy to “listen” to your network.

- Think of it like a security guard standing at the network gate, watching all the data that comes in and goes out.

**2. Checking Every Packet:**

- Every time a new packet (small piece of data) passes through the network, the program looks inside it.

- It checks if this packet contains IP information (like sender and receiver addresses).

**3. Finding TCP Packets:**

- If the packet is a TCP packet (a common type used in the internet), it also finds:

- The source port (from where the data started).

- The destination port (where the data is going).

- Ports help understand what service or app is being used, like web browsing, email, etc.

**4. Showing the Details:**

- The program then prints:

- The source and destination IP addresses.

- The source and destination port numbers (only for TCP packets).

- If it's not a TCP packet, it says: “Not a TCP packet.”

**5. Keeps Running Until You Stop:**

- The tool keeps checking and showing packet details live until you press Ctrl + C to stop it.

# Installation and Usage Guide

**Step 1: Create Virtual Environment**

``bash``

python3 -m venv sniffer_env

source sniffer_env/bin/activate

**Step 2: Install Required Library**

``bash``

pip install scapy

**Step 3: Run the Sniffer (with sudo for permissions)**

``bash``

sudo python3 network_sniffer.py

# Project Structure

``bash``

**Sniffer_project/**

- network_sniffer.py   ``# Main script file``
  
- README.md           `` # Project documentation``

- sniffer_env/         ``# Virtual environment``

