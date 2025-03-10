from LuyThua import LuyThua
import sys

def main():
    testing = ["9/25 4/2"]
    for test in testing:
        print(LuyThua(test).to_string())
if __name__ == "__main__":
    main()