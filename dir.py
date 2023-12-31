import os


def dir_print_recursive(path: str):
    dirs = os.listdir(path)
    for dir in dirs:
        p = os.path.join(path, dir)
        print(p)
        if os.path.isdir(p):
            dir_print_recursive(p)


if __name__ == "__main__":
    dir_print_recursive("/home/yozy/Downloads")
