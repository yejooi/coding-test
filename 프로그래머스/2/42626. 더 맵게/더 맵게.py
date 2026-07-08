import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while (scoville and scoville[0] < K):
        if(len(scoville) < 2):
            return -1
        fst = heapq.heappop(scoville)
        snd = heapq.heappop(scoville)
        new = fst + snd * 2
        heapq.heappush(scoville, new)
        cnt += 1
    return cnt