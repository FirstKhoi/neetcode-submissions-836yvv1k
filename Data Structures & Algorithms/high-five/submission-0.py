class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        k = 5
        all_scores = defaultdict(list)

        for item in items:
            student_id = item[0]
            score = item[1]
            heapq.heappush(all_scores[student_id], -score)

        res = []
        for student_id in sorted(all_scores.keys()):
            total = 0
            for i in range(k):
                total += - heapq.heappop(all_scores[student_id])
            res.append([student_id, total // k])

        return res