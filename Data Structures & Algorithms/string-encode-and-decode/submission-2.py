class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for size in sizes:
            res += str(size)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            curr = ""
            while s[i] != ',':
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1
        for size in sizes:
            res.append(s[i:i + size])
            i += size
        return res