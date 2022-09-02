import os
import stat

def main():
    st = os.stat('a.sh')
    os.chmod('a.sh', st.st_mode | stat.S_IEXEC)    

main()
