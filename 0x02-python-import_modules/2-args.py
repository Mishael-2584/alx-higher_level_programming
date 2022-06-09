#!/usr/bin/python3
if __name__ == "__main__":
        from sys import argv
        total = len(argv)
        if total <= 1:
            print("0 arguments.")
        else:
            if total == 2:
                 print(f"{(total - 1):d} argument:")
            else:
                print(f"{(total - 1):d} arguments:")
            for i in range(1, total):
                print(f"{i:d}: {argv[i]:s}")
