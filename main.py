from LuyThua import LuyThua
import sys

def main():
    testing = ["0/5 1/17"]
    for test in testing:
        print(LuyThua(test).to_string())
if __name__ == "__main__":
    main()