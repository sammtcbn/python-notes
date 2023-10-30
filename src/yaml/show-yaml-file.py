import yaml

def main():
    with open("example.yaml", "r") as f:
        try:
            content = yaml.safe_load(f)
            print(type(content)) # <class 'dict'>
            print(content)
            # {'fruits': {'apple': 'red', 'pear': 'green', 'banana': 'yellow'}, 'animal': {'big': {'dog': 'purple', 'rabbit': 'white'}, 'small': {'mouse': 'gray', 'bird': 'blue', 'ant': 'black'}}, 'book': {'chinese': {'book1': {'page': 100, 'author': 'sam'}, 'book2': {'page': 200, 'author': 'terry'}}, 'english': {'book3': {'page': 300, 'author': 'helen'}}}}
            print(content['fruits']['apple'])        # red
            print(content['fruits']['pear'])         # green
            print(content['fruits']['banana'])       # yellow
            print(content['animal']['small']['ant']) # black

            fruitslen = len(content['fruits'])
            print(fruitslen) # 3

            print(content['animal']['small'].items())
            # dict_items([('mouse', 'gray'), ('bird', 'blue'), ('ant', 'black')])
            print(content['animal']['small'].keys())
            # dict_keys(['mouse', 'bird', 'ant'])
            print(content['animal']['small'].values())
            # dict_values(['gray', 'blue', 'black'])

            for item in content['animal']['big'].items():
                print(item)
                print(type(item))
            # ('dog', 'purple')
            # <class 'tuple'>
            # ('rabbit', 'white')
            # <class 'tuple'>

            for key in content['book']['chinese'].keys():
                print(content['book']['chinese'][key]['author'])
            # sam
            # terry
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == '__main__':
    main()
