import requests
import sys
import getopt


# Send Slack Message Using SLack API

def send_slack_message(message):

    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                             data=payload)
    print(response.text)


def main(argv):
    message = ' '

    try:
        opts, args = getopt.getopt(argv, "hm:", ["message="])
    # h: help : print usage of the program
    # m: message
    except getopt.GetoptError:
        print("slack_message.py -m <message>")
        sys.exit(2)
    if len(opts) == 0:  # no message -> default message
        message = "HELLO, WORLD!"
    for opt, arg in opts:
        if opt == '-h':
            print('slack_message.py -m <message>')  # usage -h : help
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg

    send_slack_message(message)


if __name__ == "__main__":
    main(sys.argv[1:])
