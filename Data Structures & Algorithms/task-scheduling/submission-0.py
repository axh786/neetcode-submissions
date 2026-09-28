class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cpuCycle = 0
        char_freq = [0] * 26
        tasksHeap = []

        for task in tasks:
            char_freq[ord(task) - ord('A')] += 1
        
        for i, freq in enumerate(char_freq):
            if freq != 0:
                tasksHeap.append((-freq, chr(ord('A') + i)))
        
        heapq.heapify(tasksHeap)
        waiting = deque() # double ended queue

        while tasksHeap or waiting: # while there are tasks that are availble or in cool down keep going
            cpuCycle += 1 # this counts the current cycle regardless if it was working or idle

            if not tasksHeap and waiting: # we have this if to skip directly into to the next availle task
                cpuCycle = max(cpuCycle, waiting[0][0])

            while waiting and waiting[0][0] <= cpuCycle: # waiting[0][0] is the time that it can be used again
                ready_cycle, priority, item = waiting.popleft() # removes the entry that has been waiting the longesst
                heapq.heappush(tasksHeap, (priority, item))
            
            if tasksHeap:
                priority, item = heapq.heappop(tasksHeap) # pullout the most frequent task
                priority += 1 # remove 1 frequencey from the letter

                if priority != 0: # if the task has work left
                    waiting.append((cpuCycle+n + 1, priority, item)) # the first part of the tuple is when the task can go again


        return cpuCycle
