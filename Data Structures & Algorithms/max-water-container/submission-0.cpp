class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_val = 0;
        int l = 0, r = heights.size() - 1;
        while(l < r) {
            int minH = min(heights[l], heights[r]);
            int s = minH * (r - l);
            if(s > max_val) {
                max_val = s;
            }
            if(heights[l] <= heights[r]) {
                l++;
            } else r--;
        }
        return max_val;
    }
};
