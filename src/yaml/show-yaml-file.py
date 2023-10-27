import yaml

def main():
    with open("example.yaml", "r") as f:
        try:
            content = yaml.safe_load(f)
            print(content)
            print(content['fruits']['apple'])
            print(content['fruits']['pear'])
            print(content['fruits']['banana'])
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == '__main__':
    main()
