import sys
from interactive import interactive_mode
from noninteractive import noninteractive_mode


def main():
    if len(sys.argv) == 2:
        noninteractive_mode()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
