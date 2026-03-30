class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int l = 0, r = 31;
        while(l < r) {
            int i = (n >> l) & 1;
            int j = (n >> r) & 1;
            if(i != j) {
                n = flipBit(n, l);
                n = flipBit(n, r);
            }
            l++; r--;
        }
        return n;
    }

    int flipBit(int n, int x) {
        return n ^ (1 << x); 
    }
};
