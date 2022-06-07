import re


def main():
    with open("server.log.2018-04-04", "r") as file:
        for line in file:
            if re.compile(r"WFLYCTL\d{4}").search(line) is not None:
                print(line)


if __name__ == '__main__':
    main()
