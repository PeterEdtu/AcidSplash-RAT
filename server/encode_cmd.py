import base64
#data = "000111"
data = "agt:XP53"
encoded_bytes = base64.b64encode(data.encode("utf-8"))
encoded_string = encoded_bytes.decode("utf-8")
print(encoded_string)

# Agent for test: YWd0OlhQNTM