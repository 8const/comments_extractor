def parseSoup(soup):
    t = list(soup.stripped_strings)
    r = []
    for i in range(0, len(t)):
        if "•" in t[i]:
            name = t[i-2]
            j = i
            try:
                while not "Show less" in t[j]:
                    if not "•" in t[j]:
                        pass
                        comment = t[j]
                    j+=1
                r.append([name, comment])
            except:
                pass
    return r
