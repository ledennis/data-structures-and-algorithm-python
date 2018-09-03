def find(path, filename):
''' Assuming that the file structure consists of nodes. '''
    parent_node = directory.getNode(path)
    children = parent_node.getChildren()
    if (children):
        for child in children:
            find(child, filename);
    if filename in parent_node.getFiles():
        print('Found file in ' + path)
