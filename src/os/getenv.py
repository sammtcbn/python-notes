import os

def main():
    defaultName = "None"
    user = os.getenv("USER", defaultName)
    print("USER:", user)

    defaultShlvl = -1
    shlvl = int(os.getenv("SHLVL", defaultShlvl))
    print("SHLVL:", shlvl)

if __name__ == '__main__':
    main()
