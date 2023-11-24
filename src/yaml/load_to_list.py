import yaml

def main():
    with open("example.yaml", "r") as f:
        try:
            content = yaml.safe_load(f)
            keylist = []
            valuelist = []
            for k in content['fruits'].keys():
                keylist.append(k)
            for v in content['fruits'].values():
                valuelist.append(v)
            print(keylist)     # ['apple', 'pear', 'banana']
            print(valuelist)   # ['red', 'green', 'yellow']
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == '__main__':
    main()
