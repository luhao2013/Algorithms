/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


class Solution {
public:
    vector<int> fathers;
    int find(int i){
        int j = i;
        int temp_father = 0;
        while(fathers[i] != i){
            i = fathers[i];
        }
        while(fathers[j] != i){
            temp_father = fathers[j];
            fathers[j] = i;
            j = temp_father;
        }
        return i;
    }
    void uni(int i, int j){
        int f1 = find(i);
        int f2 = find(j);
        fathers[f1] = f2;
    }
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size() == 0 || grid[0].size() == 0){
            return 0;
        }
        int m = grid.size();
        int n = grid[0].size();
        for(int i = 0; i < m * n; i++){
            fathers.push_back(i);
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '0'){
                    continue;
                }
                int cur_pos = i * n + j;
                if(i>0 && grid[i-1][j] == '1'){
                    uni(cur_pos, cur_pos-n);
                }
                if(i<m-1 && grid[i+1][j] == '1'){
                    uni(cur_pos, cur_pos+n);
                }
                if(j>0 && grid[i][j-1] == '1'){
                    uni(cur_pos, cur_pos-1);
                }
                if(j<n-1 && grid[i][j+1] == '1'){
                    uni(cur_pos, cur_pos+1);
                }
            }
        }
        int count = 0;
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                int cur_pos = i*n +j;
                if(grid[i][j] == '1' && fathers[cur_pos] == cur_pos){
                    count++;
                }
            }
        }
        return count;
    }
};
