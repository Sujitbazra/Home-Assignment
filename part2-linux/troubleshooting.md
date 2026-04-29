PART 2: LINUX SYSTEM ADMINISTRATION
A. Troubleshooting Scenario
  - One of your web servers (10.0.1.50) is unresponsive. SSH connection times out.

Q1. How would you verify network connectivity from your jump host?
  Ans: Network Connectivity: 
      sh: ping 10.0.1.50, nc -zv 10.0.1.50 22, traceroute 10.0.1.50

Q2. Once you confirm network is working, how would you check if SSH service is running?
  Ans: From Jump Server
      sh: ssh -i key.pem ec2-user@10.0.1.50

Q3. If SSH is running but you still can’t connect, what could be the issue?
  Ans: Check SSH Service via console
      sh: sudo systemctl status sshd
      sh: sudo systemctl restart sshd

Q4. How would you check CPU, memory, and disk usage?
  Ans: CPU: top -c, htop,
       Memory: free -mh, 
       Disk Usages: df -h

Q5. How would you check recent system logs for errors?
  Ans: Firing following commands:
    sh: sudo journalctl -xe
    sh: sudo tail -n 100 /var/log/syslog
    sh: sudo tail -f 100 /var/log/messages