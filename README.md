### pwnworld : The CTF platform

## This project aims to introduce beginners to the concept of Information Security. We aim to teach Information Security to people for free through Jeopardy CTF style challenges .Currently, only easy and medium level challenges are going to be deployed. Over the time,we'' deploy hard challenges too. 
## Challenges have been created and arranged in such a way that even beginners can easily grab and enjoy the concepts of Information Security

# Completion Deadline: 15 January 2022

## Homepage : stuff/templates/challenges.html  <br><br>It must contain large, beautiful buttons of different challenge categories. For example, one Button for Web, One for Cryptography, one for pwn, one for reversing, one for IoT, one for Hardware, one for Forensics, one for OSINT, and so on. The page should also have a section with a graph between user's performance vs time. It should also have a Navigation Bar with the following clickables: My Notes, Site Activity, About, Contact, Report Bugs, Contribute

pwn means to hack, gain access over some device, web server etc.

Basic Project Layout:
Backend: Django(Main) and PHP(only for PHP related challenges) 
Database: PostgreSQL (with Django) and MySQl(with PHP)
Web Server: Apache2(for PHP challenges)

Main Directories:
challenges : Contains hacking challenges
pwnworld: The main control panel of our application
stuff: Data related to users
tools: A tool for encryption,decryption,encoding,decoding, chat application

### All html files are available in different templates folder
### All images, CSS, JS files must be placed in respective static folder

Features yet to be implemented:

1. Chat Application with markdown enabled where users can discuss stuff related to Cyber Security.
2. Note maker where users can make important notes
3. Comments, likes and dislikes with every challenge(just as in facebook)
4. Responsiveness to all pages
5. IOT, Android, Malware, Ransomware, Windows exe, Digital Forensics challenges
6. Leaderboard using web sockets
7. Graph that shows a user's performance over time
8. Graph that compares difficulty level of different categories of challenges
9. Discord server with a powerful bot for the platform
10. Webshell(the most difficult part)
11. Some way to show total number of online users
12. Blocking and ban users/ IP addresses who try to hack the CTF infrastructure
13. Protection against Cyber Attacks
