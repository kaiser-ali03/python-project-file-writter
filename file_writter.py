def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)



if  __name__  == "__main__":  # block ensures the file is written only if the script is being run directly, not imported.
    write_to_file('output.txt', 'Hello from python script ')
    print("file created and written ")

