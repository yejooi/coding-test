def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    answer = []
    
    for i, (g, n) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = n # 장르별 총 재생 수
            dic2[g] = [(i, n)] # 장르별 (고유 번호, 재생 수) 리스트
        else:
            dic1[g] += n
            dic2[g].append((i, n))
    
    for (g, n) in sorted(dic1.items(), key=lambda x: x[1], reverse=True):
        for (i, nn) in sorted(dict(dic2[g]).items(), key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)
            
    return answer