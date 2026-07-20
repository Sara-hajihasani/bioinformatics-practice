#conditions and loops
startpos=4374
endpos=8784
result=0
for x in range(startpos,endpos+1):
    if x % 2 != 0:
        result +=x
print(result)
