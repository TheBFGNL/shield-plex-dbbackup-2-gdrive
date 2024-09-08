# /usr/bin/env python3
import sys

def main():
    print(f'Hello, {sys.argv[1]}!')
    print('hello world')
    
    with open('/appl/data/test.txt', 'w') as f:
        f.write('hello world')

if __name__ == "__main__":
    main()
