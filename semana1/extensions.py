import sys

def rutaDelArchivo(str):
    if str.endswith("jpeg") or str.endswith("jpg"):
        print("images/jpeg")
    elif str.endswith("png"):
        print("images/png")
    elif str.endswith("gif"):
        print("images/gif")
    elif str.endswith("pdf"):
        print("application/pdf")
    elif str.endswith("zip"):
        print("application/zip")
    elif str.endswith("txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

def main():
    extension = input("¿Extension de el archivo? ")
    rutaDelArchivo(extension)



if __name__ == "__main__":
    sys.exit(main())