# Lab 01: Using Sockets

## Overview
In this lab, you'll prepare your development environment and write a simple server application in Python 3 using the Berkeley sockets API. You may use your own machine or a department machine for lab.

### Learning objectives
After completing this lab, you should be able to:
* Use the Berkeley sockets API to send/receive data over the network
* Use netcat and netstat to debug a program that uses sockets

## Part 1: Prepare your development environment
We will be using the CS department's "tigers" pool of Linux servers for all our work this semester. You must be **connected to the `Eduroam` wireless network, or use VPN with the `FullTunnel` gateway,** to access the servers.

Aaron will officially support the following two development environments:
* Microsoft Visual Studio Code (VS Code) with the Remote - SSH extension
* A terminal with SSH and a command-line text editor (e.g., Vim or Nano)

### Option 1: Microsoft VS Code
If you are using your own machine to access the servers, [download](https://code.visualstudio.com) and install VS Code. If your computer is running Windows 10, you will also need to install the [OpenSSH client](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).

Note: VS Code and SSH are already installed on all department machines.

After you have installed VS Code:
1. Click on the <img src="https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extensions-view-icon.png" width="30px"> icon on the left of the VS Code window. 
2. Search for the `Remote - SSH` extension in the left panel, and click `Install` on the top of the right panel. 
3. Click the opposing arrows icon in the lower-left of your VS Code window:

    ![Screenshot of Remote Development icon in VS Code](https://microsoft.github.io/vscode-remote-release/images/remote-dev-status-bar.png)

4. In the command palette at the top of the VS Code window, select `Connect to Host...`, then `Add new SSH Host`. 
5. Fill in the command `ssh YOU@tigers.cs.colgate.edu`, replacing `YOU` with your CS username. 
6. When asked which SSH configuration file to update, select the file located in your user directory (usually the first file in the list).

To connect to the servers:
1. Click on the opposing arrows icon, in the lower-left corner of your VS Code window. 
2. Choose `Connect to Host...`, then select `tigers.cs.colgate.edu`. 
3. If prompted, select `Continue` to connect to `tigers.cs.colgate.edu` with fingerprint `SHA256:Fx96G/IqfDhj3vXjsVW3DQMRkcS9CYKgUJGFJoWcJ8Q`
4. Enter your CS password.
5. After you are connected, `SSH: tigers.cs.colgate.edu` will appear after the opposing arrows icon in the lower-left of your VS Code window.

For additional information and help with the VS Code SSH remote editing capability, click the opposing arrows icon in the lower left, then choose the menu option `Remote-SSH: Help`.

### Option 2: Terminal with SSH and a command-line text editor
If your computer is running Windows 10, you will need to install the [OpenSSH client](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).

To connect to the servers:
1. Open the `Terminal` program on Mac OS, the `Command Prompt` on Windows, or another terminal application supported by your operating system
2. Enter the command `ssh YOU@tigers.cs.colgate.edu`, replacing `YOU` with your CS username. 
3. If prompted, enter `yes` to connect to `tigers.cs.colgate.edu` with fingerprint `SHA256:Fx96G/IqfDhj3vXjsVW3DQMRkcS9CYKgUJGFJoWcJ8Q`
4. Enter your CS password. (Note: you won't see any characters when you enter your password.)
5. After you are connected, your command prompt should change to `YOU@bengal` or `YOU@caspian` (where `YOU` is your CS username).

For help using Vim, see [Getting Started With Vim](https://medium.com/swlh/getting-started-with-vim-3f11fc4f62c4).

For help using Nano, see [The Beginnger's Guide to Nano, the Linux Command-Line Text Editor](https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/).

### Configure git
You must configure your git environment on the servers for this course. After you have connected to the servers, enter the following commands (**excluding the dollar sign (`$`) and substituting your own name and email**):
```bash
$ git config --global user.name "James Mickens"
$ git config --global user.email "mickens@fas.harvard.edu"
$ ssh-keygen -f ~/.ssh/id_rsa -N ""
$ cat ~/.ssh/id_rsa.pub 
```

(Note: [James Mickens](https://mickens.seas.harvard.edu) is a black computer scientist known for his research on the performance, security, and reobustness of large-scale distributed web services.)

The last command will display your newly generated public key. Copy the entire key, then go to [https://github.com/settings/keys](https://github.com/settings/keys). Click `New SSH key`, enter `COSC 465` for the title, and paste the copied key into the `Key` textbox. Click `Add SSH key`.

## Part 2: Knock, Knock Server
You will write a server application that responds to knock, knock jokes. 

A knock, knock joke has the following sequence:
```
Knock, Knock
Who's there?
WORD
WORD who?
PUNCHLINE
Ha, ha, ha!
```
For example,
```
Knock, Knock
Who's there?
Spell
Spell who?
Okay, S-P-E-L-L
Ha, ha, ha!
```

A client will send the first, third, and fifth lines to the server; the server will send the second, fourth, and sixth lines to the client (after receiving the preceding line).

### Step 1: Establishing a connection
The knock, knock server is started using the following command:
```
./knock.py -p PORT
```
where `PORT` is replaced with the port number (an integer between 1 and 65535) on which the server is waiting for a connection.

You should call the appropriate socket functions in the `main` function to allow a client to connect to the knock, knock server.

#### Testing
You can use the program `netcat` to help you test your code. First, start your knock, knock server using a randomly choosen port number between `5000` and `65000`. Then, in a separate terminal window connected to the same tigers server, start `netcat` using the following command:
```bash
netcat -v 127.0.0.1 PORT
```
replacing `PORT` with the same port number you specified when you started your knock, knock server.

If your server is working correctly, netcat should output a message similar to the following:
```bash
Connection to 127.0.0.1 5000 port [tcp/*] succeeded!
```
If netcat outputs an error, then there is a problem with your code. 

You can use `netstat` to list all active connections:
```bash
netstat -t
```
If you also include the `-l` (lowercase L) option, then `netstat` will list all listening connections.

You can end both your knock, knock server and `netcat` using `Ctrl+c.` It may take up to two minutes before you can reuse the same port number, so you may need to switch port numbers if you run your application multiple times in quick succession.

### Step 2: Receiving/sending messages
Now, add code to your knock, knock server to receive messages from the client and send responses. Your server will need to receive three messages from the client (`Knock, knock`, `WORD`, and `PUNCHLINE`), and send three messages to the client (`Who's there?`, `WORD who?` and `Ha, ha, ha!`). 

It is important that the client and server conform to the "protocol" of a knock, knock joke. In other words, the server should only accept `Knock, knock` as the first message from the client. If the server sends something else, then the server should respond `I don't understand` and close the connection. There is no way to validate the second and third messages from the client (`WORD` and `PUNCHLINE`), so the server should accept whatever text the client sends.

You should also call the appropriate socket function(s) functions to gracefully terminate the socket connection(s) after sending the last message (`Ha, ha, ha!`).

#### Testing
Again, you can use netcat to help you test your knock, knock server. Start netcat and your knock, knock application as discussed in Step 1. After a connection is established, you should be able to type a message in netcat, hit enter, and the server should recieve the message. Likewise, when the server sends a message, `netcat` should display the message. 

To test your messenger application with itself: start one instance of your application in server mode (as discussed in Part 1) and another instance of your application in client mode (as discussed in Part 1). You should be able to send and receive messages between the messenger applications in the same way you send and receive messages between the messenger application and netcat (described in the preceding paragraph).

## Submission instructions
1. Commit and push your code to GitHub
2. Fill-out [this Google form](https://forms.gle/XWb71PSum18ZAfjo6)