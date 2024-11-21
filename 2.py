from pwn import *
import json

r = remote('socket.cryptohack.org', 13377)

for _ in range(100):
    data = r.recvline().strip()
    data = json.loads(data)
    encoding, encoded = data['type'], data['encoded']

    if encoding == "base64":
        encoded = base64.b64encode(self.challenge_words.encode()).decode() # wow so encode
    elif encoding == "hex":
        encoded = self.challenge_words.encode().hex()
    elif encoding == "rot13":
        encoded = codecs.encode(self.challenge_words, 'rot_13')
    elif encoding == "bigint":
        encoded = hex(bytes_to_long(self.challenge_words.encode()))
    elif encoding == "utf-8":
        encoded = [ord(b) for b in self.challenge_words]

    res = json.
    r.sendline()
