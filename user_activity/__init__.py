from .main import get_events

__version__ = "0.0.1"

def run():
    """ Command line Interface """
    report = get_events()
    print(report)
    return