with open("create-1m-bin.bin", "wb+") as fp:
  fp.seek(0)
  fp.write(b'\xFF'*1*1024*1024)
