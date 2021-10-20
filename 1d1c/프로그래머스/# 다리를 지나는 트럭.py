# 다리를 지나는 트럭.py
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    trucks_on_bridge = deque([0]*bridge_length)
    w = 0
    
    while len(trucks_on_bridge) :
        time += 1
        w -= trucks_on_bridge.popleft()
        if truck_weights:
            if w + truck_weights[0] <= weight:
                tmp = truck_weights.popleft()
                w += tmp
                trucks_on_bridge.append(tmp)
            else:
                trucks_on_bridge.append(0)
    return time