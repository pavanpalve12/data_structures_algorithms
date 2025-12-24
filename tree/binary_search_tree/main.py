from tree_api import TreeAPI

def generate_test_tree(tree):
    #tree = TreeAPI(10)
    print(tree)

def main():
    tree = TreeAPI()
    generate_test_tree(tree)

if __name__ == '__main__':
    main()