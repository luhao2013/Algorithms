/*
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

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
    void solve(vector<vector<char>>& board){
        if(board.size() == 0 || board[0].size() == 0){
            return;
        }
        int m = board.size();
        int n = board[0].size();
        int dummy_pos = m * n;  // 用来做为四周节点的父节点，下面vector数组多一个值
        for(int i = 0; i <= m * n; i++){
            fathers.push_back(i);
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 'X'){
                    continue;
                }
                int cur_pos = i * n + j;
                if(i == 0 || j == 0 || i == m-1 || j == n-1){
                    uni(cur_pos, dummy_pos);
                    continue;
                }
                if(board[i-1][j] == 'O'){
                    uni(cur_pos, cur_pos-n);
                }
                if(board[i+1][j] == 'O'){
                    uni(cur_pos, cur_pos+n);
                }
                if(board[i][j-1] == 'O'){
                    uni(cur_pos, cur_pos-1);
                }
                if(board[i][j+1] == 'O'){
                    uni(cur_pos, cur_pos+1);
                }
            }
        }
        int dummy_father = fathers[dummy_pos];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 'X'){
                    continue;
                }
                int cur_pos = i * n + j;
                if(find(cur_pos) != dummy_father){
                    board[i][j] = 'X';
                }
            }
        }
    }
};
