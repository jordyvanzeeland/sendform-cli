import argparse
from sendformdata import Clients

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

list_skills_subparser = subparsers.add_parser('list-clients')
list_skills_subparser.set_defaults(func=Clients.list_clients)

skills_subparser = subparsers.add_parser('create-client')
skills_subparser.set_defaults(func=Clients.insert_client)
skills_subparser.add_argument('--name')
skills_subparser.add_argument('--domain')
skills_subparser.add_argument('--mailto')

def main():
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()