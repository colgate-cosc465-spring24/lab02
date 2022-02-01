from argparse import ArgumentParser

def main():
    # Parse arguments
    arg_parser = ArgumentParser(description="Knock, knock server")
    arg_parser.add_argument("-p", "--port",
            type=int, required=True, help="Port to listen on")
    settings = arg_parser.parse_args()

    print("Running knock, knock server on port {}".format(settings.port))

    # TODO

if __name__ == '__main__':
    main()