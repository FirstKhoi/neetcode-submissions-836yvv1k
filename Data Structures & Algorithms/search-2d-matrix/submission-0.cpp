class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if(m == 0) return false;

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < matrix[i].size(); j++) {
                if(matrix[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
};
