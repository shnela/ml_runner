import os


if __name__ == '__main__':
    print(__file__)
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    print(os.path.join(current_dir, '..'))
    print(os.path.join(current_dir, 'subdir1', 'subdir2'))
