try:
    with open("plik1.txt", 'r') as file1:
        with open("plik2.txt", 'w') as file2:
            for linia in file1:
                file2.write(linia)
except IOError as ioe:
    print("Wystapil blad! {}".format(ioe))
