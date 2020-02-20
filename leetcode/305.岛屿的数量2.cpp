/*
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation 1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation 2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation 3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation 4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
*/

#include <vector>

class Solution{
public:
    vector<int> fathers;
    int find(int i){
        int j = i;
        int temp_father;
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

    int uni(int i, int j){
        int f1 = find(i);
        int f2 = find(j);
        if(f1 == f2){
            return 0;
        }
        fathers[f1] = f2;
        return 1;
    }

    vector<int> numsIslands2(int m, int n, vector<vector<int>>& positions){
        vector<vector<char>> grid(m, vector<char>(n));
        for(int i = 0; i < m * n; i++){
            fathers.push_back(i);
        }
        int count = 0;
        vector<int> result;
        for(vector<int> position : positions){
            int i = position[0];
            int j = position[1];
            // 有可能会有重复
            if(grid[i][j] == '1'){
                result.push_back(count);
                continue;
            }
            grid[i][j] = '1';
            count++;
            int cur_pos = i * n + j;
            if(i >0 && grid[i-1][j] == '1'){
                if(uni(cur_pos, cur_pos - n)){
                    count--;
                }
            }
            if(i <m-1 && grid[i+1][j] == '1'){
                if(uni(cur_pos, cur_pos + n)){
                    count--;
                }
            }
            if(j >0 && grid[i][j-1] == '1'){
                if(uni(cur_pos, cur_pos - 1)){
                    count--;
                }
            }
            if(j < n-1 && grid[i][j+1] == '1'){
                if(uni(cur_pos, cur_pos + 1)){
                    count--;
                }
            }
            result.push_back(count);
        }
        return result;
    }


};
