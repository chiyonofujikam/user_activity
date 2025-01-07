
import sys

import requests
from .parser_event import EventParser

GITHUB_URL = "https://api.github.com/users/<username>/events"

def get_args() -> str:
    """ returns the username """
    if (args_count := len(sys.argv)) > 2:
        print(f"One argument expected, got {args_count - 1}")
        raise SystemExit(2)
        return ''

    elif args_count < 2:
        print("You must specify a Username")
        raise SystemExit(2)
        return ''

    return sys.argv[1]

def get_events():
    """ fetch data """
    username = get_args()
    if not username:
        return

    url = GITHUB_URL.replace('<username>', username)
    response = requests.get(url)

    if response.status_code == 503:
        print("Service unavailable")
        return

    if response.status_code == 403:
        print("Event is Forbidden")
        return

    if response.status_code == 304:
        print("Not modified")
        return

    if response.status_code == 404:
        print(f" The Username : {username} isn't found\n response: \n{response}")
        return

    if response.status_code != 200:
        print("Error !")
        return

    events = response.json()
    if not events:
        print(f"No Data retrieved of : {username}")
        return

    return EventParser(events).report