
import json
import pyAesCrypt

BUFFER_SIZE = 64 * 1024
PASSWORD = "secretpass"

def encrypt_data(data, filename):
    tmp_file = filename + ".tmp"
    with open(tmp_file, 'w') as f:
        json.dump(data, f)
    pyAesCrypt.encryptFile(tmp_file, filename, PASSWORD, BUFFER_SIZE)
    os.remove(tmp_file)

def decrypt_data(filename):
    tmp_file = filename + ".tmp"
    try:
        pyAesCrypt.decryptFile(filename, tmp_file, PASSWORD, BUFFER_SIZE)
        with open(tmp_file, 'r') as f:
            data = json.load(f)
        os.remove(tmp_file)
        return data
    except Exception:
        return {}
