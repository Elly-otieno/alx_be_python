def openFile(file):
    try:
        with open(file, 'rb') as f:
            data = f.read()
            print(f"PDF '{file}' opened successfully. Size: {len(data)} bytes.")
            return data
    except FileNotFoundError as e:
        print(f'Error: {e}')

data = openFile('eokoertth_cv.pdf')