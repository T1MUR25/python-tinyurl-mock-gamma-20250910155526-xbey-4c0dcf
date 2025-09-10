import hashlib
s='gammalab'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
