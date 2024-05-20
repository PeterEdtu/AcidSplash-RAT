from base64 import b64decode, b64encode

def encode(data:str) -> str:
    encoded_bytes = b64encode(data.encode("utf-8"))
    return encoded_bytes.decode("utf-8").replace('==', '')

def decode(data:str)-> str:
    if "==" not in data:
        data+="=="
    decoded_str = b64decode(data)
    return decoded_str.decode("utf-8")
