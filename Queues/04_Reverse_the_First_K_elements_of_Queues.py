
from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    if (inputQueue.empty()) or (k > inputQueue.qsize()) :
        return inputQueue
    
    if k <= 0 :
        return inputQueue
    
    stack = list()

    for i in range(k) :
        stack.append(inputQueue.get())


    while not isEmpty(stack) :
        inputQueue.put((stack.pop()))

    for i in range(inputQueue.qsize() - k) :
        inputQueue.put(inputQueue.get())


    return inputQueue





