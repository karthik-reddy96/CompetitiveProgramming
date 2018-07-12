need = {}
def needed(egg, floor):
    if (egg, floor) in need:
        return needed[(egg, floor)]
    if egg == 1:
        return floor
    if egg > 1:
        low = floor
        for f in range(floor):
            resultIfEggBreaks = need(egg - 1, f)
            resultIfeggurvives = need(egg, floor - (f + 1))
            result = max(resultIfEggBreaks, resultIfeggurvives)
            if result < low:
                low = result
        need[(egg, floor)] = 1 + low
        return 1 + low
print (needed(2, 100)