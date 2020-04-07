/*
Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

 

Example 1:

Given matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


// 1 原地旋转，还有翻转可以做这题
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n / 2; ++i) {
            for (int j = 0; j < (n + 1) / 2; ++j) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = temp;
            }
        }
    }
};

// 2 使用辅助数组
// class Solution {
// public:
//     void rotate(vector<vector<int>>& matrix) {
//         int row = matrix.size();
//         int col = matrix[0].size();
//         // 原先这种初始化方法比较麻烦
//         // vector<vector<int>> res(col, vector<int>(row));
//         // C++ 这里的 = 拷贝是值拷贝，会得到一个新的数组
//         // 不过因为这里是方阵，所以才能这么用
//         auto res = matrix;
        
//         for(int i=0; i<row; i++){
//             for(int j=0; j<col; j++){
//                 res[j][row-1-i] = matrix[i][j];
//             }
//         }
//         matrix = res;
//     }
// };