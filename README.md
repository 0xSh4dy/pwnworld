# pwnworld: The hacking, CTF platform

#### pwn means to gain access or hack some computer, website, service, etc.

##### pwnworld is a platform where both , beginners and advanced level players can practice their skills in Cyber Security (both cyber attack and defense).This platform will contain hundreds of challenges, at least 20 from each category. Different categories are : Binary Exploitation, Reverse Engineering, Web Exploitation, Digital Forensics, Jailbreak and Cryptography.

##### Frameworks, Technology to be used:

Frontend : HTML, CSS ,JS(basic JS with Fetch API).You may use TypeScript for avoiding JS bugs,
            but it is not necessary.
Template Engine: Jinja2

Backend: Flask (Python)

Database: MongoDB(main database) and SQLite(For SQL Injection Challenges)

Development Environment: You may do it on Windows,but I strongly recommend Linux because of the power you get on it. Although it depends on your choice, use Windows if you like it.

Basic Work:
### Rakshit: Webshell, database admin, backend, challenge creator, penetration testing
### Rishav: Design,backend, frontend(HTML,CSS), database operations
### Rishabh: Frontend(HTML,CSS, JS, Templates), updating README.md
### Prabal: Frontend(HTML,CSS, JS, Templates), updating README.md


Note: The homepage must contain a navigation bar. The navigation bar should contain Home, Webshell, About, Contact Us. In the body, it should have two options: Beginner and Advanced such that on clicking Beginner, beginner challenges appear on the screen. Same rule applies for Advanced challenges. The site must be in dark mode. The homepage will also contain a side table with options for 5 different categories of challenges. On clicking a particular category, challenges of that category must appear.

Each challenge should show the difficulty level and the number of users that have solved it.

Starting steps:
#### Rakshit start developing the Webshell.
#### Rishav will create the design for the login, signup and homepage. 
#### Rishabh and Prabal will start coding the login, signup and homepage after the design is completed.

This is the basic work. Next steps will be decided after this part has been completed.

API endpoints:

/home   : homepage
/about  : about
/webshell : webshell
/contact  : contact us
/leaderboard   : leaderboard
/challenges/web-exploitation/challengeName      :For Web-Exploitation
/challenges/rev/challengeName                   :For Reverse Engineering
/challenges/binary-exploitation/challengeName   : For pwn(Binary Exploitation)
/challenges/forensics/challengeName             : For digial forensics
/challenges/cryptography/challengeName          : For cryptography
/challenges/jailbreak/challengeName             : For jailbreak


# Important Note: Do not push your code on the master branch. Create a separate branch, with the branch name as your name and then push code into it. 

## To start working, clone the repository and create files there
Create html files in the templates folder.
Create JS and CSS files in the js and css folder in the static folder respectively.
Add icons, images in the images folder.
The challenges folder will contain the code of the challenges.














