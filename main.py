import hashlib
s='litenet'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
