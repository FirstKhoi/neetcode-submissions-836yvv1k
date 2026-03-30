class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert_map = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        rotate_number = []

        for ch in str(n):
            if ch not in invert_map:
                return False

            rotate_number.append(invert_map[ch])

        rotate_number = "".join(rotate_number[::-1])
        return int(rotate_number) != n