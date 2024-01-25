#!/usr/bin/python3

#####
# COSC 465: Computer Networks, Spring 2024
# Lab 02: Using sockets
#####

from argparse import ArgumentParser

MAX_MESSAGE_LENGTH = 280

def main():
    # Parse arguments
    arg_parser = ArgumentParser(description="Knock, knock server")
    arg_parser.add_argument("-p", "--port",
            type=int, required=True, help="Port to listen on")
    settings = arg_parser.parse_args()

    print("Running knock, knock server on port {}".format(settings.port))

    # TODO
    return

def handle_client(sock):
    # TODO
    return

if __name__ == '__main__':
    main()