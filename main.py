from LuyThua import LuyThua
import sys

def main():
    testing = ["4/9 1/12", "15/3 9/7", "-1/7 -9/7", "0/7 0/0"]
    for test in testing:
        print(LuyThua(test).to_string())
if __name__ == "__main__":
    main()