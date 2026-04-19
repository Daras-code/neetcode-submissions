class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencylist = Counter(tasks)
        max_freq = max(frequencylist.values())
        count_max = sum(1 for v in frequencylist.values() if v == max_freq)

        min_cycles = (n+1)*(max_freq - 1) + count_max
        return max(min_cycles, len(tasks))
