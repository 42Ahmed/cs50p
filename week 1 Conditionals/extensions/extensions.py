file = input("File name: ").strip().lower()

dot = file.rfind(".")

if dot == -1:
    print("application/octet-stream")
else:
    ext = file[dot+1:]

    if ext == "gif":
        print("image/gif")
    elif ext == "jpg" or ext == "jpeg":
        print("image/jpeg")
    elif ext == "txt":
        print("text/plain")
    elif ext == "pdf":
        print("application/pdf")
    elif ext == "zip":
        print("application/zip")
    elif ext == "png":
        print("image/png")
    else:
        print("application/octet-stream")

