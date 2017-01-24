import sys
from model import do 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    do.echo(sys.argv[1])
