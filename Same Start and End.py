stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
thing = 0
for s in stringsList:
    if len(s) > 0:
        if s[0].lower() == s[-1].lower():
            thing += 1
print(thing)
