import sys

ngram = {}


def read_text(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines if line.strip()]
        return lines

def get_ngrams(lines):
    n = 2
    for line in lines:
        while n <= len(line):
            for index in range(len(line)-n+1):
                get_string = ' '.join(line[index:index+n])
                if get_string in ngram:
                    ngram[get_string] += 1
                else:
                    ngram[get_string] = 1
            n += 1
        n = 2


def find_longest():
    max_n = 0
    longest_keys = []
    for key, value in ngram.items():
        if value == 1:
            continue
        else:
            if len(key.split()) > max_n:
                max_n = len(key.split())
                longest_keys = [key]
            elif value == max_n:
                longest_keys.append(key)
    print("The longest ngrams is", longest_keys, "with number of tokens", max_n)


def main():
    filename = sys.argv[1]
    lines = read_text(filename)
    get_ngrams(lines)
    find_longest()


if __name__ == "__main__":
    main()
