# Lab 02: Using Sockets

## Overview
In this lab, you'll write a simple server application in Python that using the Berkeley sockets API and responds to knock, knock jokes.

### Learning objectives
After completing this lab, you should be able to:
* Use the Berkeley sockets API to send/receive data over the network
* Use netcat to debug a program that uses sockets

## Getting Started
Clone your git repository on a tigers server.

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

## Step 1: Establishing a connection
The knock, knock server is started using the following command:
```
./knock.py -p PORT
```
where `PORT` is replaced with the port number (an integer between 1 and 65535) on which the server is waiting for a connection.

Add calls to the appropriate socket functions in the `main` function in `knock.py` to allow a client to connect to the knock, knock server.

### Testing
You can use the program `netcat` to help you test your code. First, start your knock, knock server using a **randomly chosen port number between `5000` and `65000`**. Then, in a separate terminal window, start `netcat` using the following command:
```bash
netcat -v 127.0.0.1 PORT
```
replacing `PORT` with the same port number you specified when you started your knock, knock server.

If your server is working correctly, netcat should output a message similar to the following:
```bash
Connection to 127.0.0.1 5000 port [tcp/*] succeeded!
```

You can end both your knock, knock server and `netcat` using `Ctrl+c.` It may take up to two minutes before you can reuse the same port number, so you **may need to switch port numbers if you run your application multiple times in quick succession**.

## Step 2: Receiving/sending messages
Now, add code to the `handle_client` function in `knock.py` to receive messages from the client and send responses. Your server will need to receive three messages from the client (`Knock, knock`, `WORD`, and `PUNCHLINE`), and send three messages to the client (`Who's there?`, `WORD who?` and `Ha, ha, ha!`). 

It is important that the client and server conform to the "protocol" of a knock, knock joke. In other words, the server should only accept `Knock, knock` as the first message from the client. If the server sends something else, then the server should respond `I don't understand` and close the connection. There is no way to validate the second and third messages from the client (`WORD` and `PUNCHLINE`), so the server should accept whatever text the client sends.

You should also call the appropriate socket function to gracefully terminate the connection after sending the last message (`Ha, ha, ha!`).

Remember to add a call to `handle_client` in `main`.

### Testing
Again, you can use `netcat` to help you test your knock, knock server. Start `netcat` and your knock, knock server as discussed in Step 1. After a connection is established, you should be able to type a message in `netcat`, hit enter, and the server should receive the message. Likewise, when the server sends a message, `netcat` should display the message. 

Note: `netcat` will not automatically end after the server has sent the last line (`Ha, ha, ha!`) and closed the connection. `Ctrl+d` will gracefully terminate `netcat`.

## Step 3: Handling multiple clients
Now, add code to the `main` function in `knock.py` to create a [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor). Update `main` to accept connections from clients indefinitely. Each time a client connects, call the `submit` function on the created `ThreadPoolExecutor` to invoke the `handle_client` function for the connected client.

### Testing
Run multiple instances of `netcat` at the same time (in different terminals) to test that your knock, knock server properly handles multiple clients in parallel.

## Self-assessment
The self-assessment for this lab will be available on Moodle after 5pm on Thursday, February 1. Please complete the self-assessment by 11pm on Monday, February 5.