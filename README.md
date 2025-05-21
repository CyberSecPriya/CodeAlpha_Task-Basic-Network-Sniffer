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

# Setting Up Virtual Environment

 1.  Create a virtual environment:

      ``bash``

      python3 -m venv sniffer_env

2.  Activate the virtual environment:

      ``bash``

      source sniffer_env/bin/activate

3.  Install Scapy inside the virtual environment:

     ``bash``

     pip install scapy

 # How to Run

1. Open terminal (Ubuntu/WSL or any Linux environment).
   
2. Navigate to the project folder:
   
   ```bash
   cd "your/project/folder/path"

3. Run the Python script with sudo (root access is required for sniffing):

  ``bash``

   sudo python3 network_sniffer.py

# Output

When the script is run, it starts monitoring the network for real-time packets. Each time a packet is captured, it displays the source and destination IP addresses.

![Image](https://github.com/user-attachments/assets/0c2446aa-5d77-4bbc-8871-11e9b4123152)

This means a packet was detected from IP ``172.21.218.49 to 185.125.190.56``, but it was not using the TCP protocol-so port numbers were not displayed. The script is programmed to check if the packet is a TCP packet and only then show port numbers. If it’s not TCP, it simply shows the message "Not a TCP packet."

This output helps in identifying and analyzing real-time IP traffic on the network.

# Features Implemented
- Real-time packet sniffing

- Extracting IP addresses

- Detecting TCP packets

- Displaying port numbers

- Console-friendly output with separators

# References

These resources helped me understand concepts and complete the task successfully:

- [**Scapy Official Documentation**](https://scapy.readthedocs.io/en/latest/):  
  Used to understand how to capture packets, extract IP and TCP layers, and use the `sniff()` function.

- [**Python Virtual Environments (venv)**](https://docs.python.org/3/library/venv.html):  
  Helped me create and manage a clean environment to install and run Scapy safely.

- **General research and experimentation**:  
  I searched online, tested different code snippets, and learned through trial and error to fix issues and improve the script during my internship.

# Note

- This project is created as part of my internship learning tasks and is meant for educational purposes only.

- Packet sniffing should always be done in ethical and legal environments. Always ensure you have permission to monitor a network.

- Run the script with administrator/root privileges to capture network packets properly.

# Conclusion

This project gave me hands-on experience in building a basic network sniffer using Python and Scapy. I learned how network traffic flows and how packets are structured and captured in real time. While the project was challenging at first, it helped me understand the core concepts of packet analysis, TCP/IP layers, and how tools like Scapy work behind the scenes.

Overall, it was a valuable learning experience that improved my confidence and practical skills in cybersecurity and network monitoring.
