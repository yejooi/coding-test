def solution(sizes):
    wMax = 0
    hMax = 0
    
    for (w, h) in sizes:
        if w < h:
            w, h = h, w
        if w > wMax:
            wMax = w
        if h > hMax:
            hMax = h
        
    return wMax * hMax