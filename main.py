import argparse
import data

def run():
    my_parser = argparse.ArgumentParser(description='analysis the json file')
    my_parser.add_argument('-i', '--init', help='json file path')
    my_parser.add_argument('-u', '--user', help='username')
    my_parser.add_argument('-r', '--repo', help='repository name')
    my_parser.add_argument('-e', '--event', help='type of event')
    args = my_parser.parse_args()

    if args.init:
        my_data = data.Data(path=args.init)
    else:
        my_data = data.Data()
        if args.event:
            if args.user:
                if args.repo:
                    print(my_data.get_cnt_user_and_repo(args.user, args.repo, args.event))
                else:
                    print(my_data.get_cnt_user(args.user, args.event))
            else:
                if args.repo:
                    print(my_data.get_cnt_repo(args.repo, args.event))
                else:
                    print("missing argument: user or repo")
        else:
            print("missing argument: event")



if __name__ == '__main__':
    run()