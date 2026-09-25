class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        # Count frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put numbers into buckets based on frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Get k most frequent elements
        answer = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                answer.append(num)

                if len(answer) == k:
                    return answer

        return answer
        