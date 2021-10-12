from Crypto.Util.number import getPrime,bytes_to_long,long_to_bytes,inverse

f = open("flag.txt",'r').read()
n = 379557705825593928168388035830440307401877224401739990998883
e = 65537
p =  564819669946735512444543556507
q =  671998030559713968361666935769
phi = (p-q)*(q-1)
d = inverse(e,phi)
m = bytes_to_long(f.encode())
ct = pow(m,e,n)
print(ct)
