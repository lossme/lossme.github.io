import os


def walk(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        # for dirname in dirnames:
        #     yield dirname
        for filename in filenames:
            yield os.path.join(parent, filename)


def main():
    rootdir = 'source'
    content = '\n'.join(
        map(
            lambda file: '- [{}]({})'.format(os.path.basename(file).split('.', 1)[0], file), walk(rootdir))
    )
    with open('index.md', 'w') as f:
        f.write(content)
        f.write('\n')


if __name__ == '__main__':
    main()
