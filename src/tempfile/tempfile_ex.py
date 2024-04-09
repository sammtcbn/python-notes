import tempfile

def main():

    with tempfile.NamedTemporaryFile() as tmp:
        print(tmp.name)

if __name__ == '__main__':
    main()

# Result:
# $ python tempfile_ex.py
# /tmp/tmpg3bst6wo
# $ python tempfile_ex.py
# /tmp/tmp0pgyq2n4
# $ python tempfile_ex.py
# /tmp/tmpmmak4cbl
