def reverse_complement(Pattern):
    Pattern = reverse(Pattern)
    Pattern = complement(Pattern)
    return Pattern
def reverse(Pattern):
    rev = ""
    for char in Pattern:
     rev=char+rev
    return rev
def complement(Pattern):
    comp=""
    for char in Pattern:
        if char=="A":
            comp=comp+"T"
        elif char=="T":
            comp=comp+"A"
        elif char=="C":
            comp=comp+"G"
        elif char=="G":
            comp=comp+"C"
    return comp
Pattern=sys.stdin.read().strip().replace("/n","")
result=reverse_complement(Pattern)
print(result)
