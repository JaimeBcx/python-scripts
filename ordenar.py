import os
import pathlib
import shutil

rutadir = os.getcwd()

directorio = pathlib.Path(rutadir)

for i in directorio.iterdir():
    
    carpeta = i.suffix.split(".").pop()

    if os.path.isdir(i):
        pass
    elif os.path.isfile(i) and carpeta == "":
        os.mkdir("sin_extension")
        shutil.move(i.name, "sin_extension")
    else:
        testeo = os.path.exists(carpeta)
        if testeo == False:
            os.mkdir(carpeta)
        shutil.move(i.name, carpeta)

