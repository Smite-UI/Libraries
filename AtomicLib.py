import os
import threading

class file:
    def __init__(self):

        FileName = ""
        data = ""
        file_lock = threading.Lock()

    def atomicwrite(path, data):
        temp = ".tmp" + path
        mode = "w"

        with open(temp, mode) as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)

    def atomicread(path: str):
        _read_lock = threading.Lock()

        with _read_lock:
            with open(path, "r") as f:
                read = f.read()
                return read

    def check(FileName):
        mode = "r"
        NO_FILE = "Specified File Does Not Exist"
        FOUND_FILE = "File found"
        
        try:
            with open(FileName, mode) as f:
                return FOUND_FILE
        except:
            return NO_FILE

    
    def atomicdel(path: str):
        global file_lock
        with file_lock:
            try:
                os.remove(path)
            except FileNotFoundError:
                pass

class binaryfile:
    def __init__(self):

        FileName = ""
        data = ""
        
    def writebinary(path: str, data: bytes | str):
        temp = path + ".tmp"
        mode = "wb" if isinstance(data, bytes) else "w"

        _write_lock = threading.Lock()

        with _write_lock:
            with open(temp, mode) as f:
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
            os.replace(temp, path)
        
    def readbinary(path: str):
        _read_lock = threading.Lock()
        
        with _read_lock:
            with open(path, "rb") as f:
                read_info = f.read()
                return read_info
        
    