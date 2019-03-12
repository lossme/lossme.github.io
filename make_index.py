import os
import collections
import itertools


def walk_md(rootdir):
    Item = collections.namedtuple("Item", ["filename", "filepath", "category"])

    item_list = []
    for parent, dirnames, filenames in os.walk(rootdir):
        # for dirname in dirnames:
        #     yield dirname
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(parent, filename)
                item = Item(filename=filename, filepath=filepath, category=os.path.split(parent)[1])
                item_list.append(item)
    item_list.sort(key=lambda item: item.category)
    return item_list


def main():
    rootdir = 'source'
    item_list = walk_md(rootdir)
    with open('index.md', 'w') as f:
        for category, items in itertools.groupby(item_list, key=lambda item: item.category):
            f.write("## {}\n\n".format(category))
            for item in items:
                line = ' - [{filename} {category}]({filepath})\n'\
                    .format(filename=item.filename, category=item.category, filepath=item.filepath)
                f.write(line)
            f.write("\n\n")


if __name__ == '__main__':
    main()
    # for i in walk_md("source/"):
    #     pass
