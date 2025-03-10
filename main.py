from LuyThua import LuyThua
import sys

def main():
    testing = ["3/5 0/17"]
    for test in testing:
        print(LuyThua(test).to_string())
if __name__ == "__main__":
    main()