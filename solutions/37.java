//https://leetcode.com/problems/sudoku-solver/description/?envType=daily-question&envId=2025-08-31 37 {

class Solution {
    public void solveSudoku(char[][] board) {
        solve(board, 0, 0);
    }

    public boolean solve(char[][] board, int row, int col) {
        for (int i = row; i < 9; i++, col = 0) {
            for (int j = col; j < 9; j++) {
                if (board[i][j] != '.') {
                    continue;
                }
                for (char num = '1'; num <= '9'; num++) {
                    if (isValid(board, i, j, num)) {
                        board[i][j] = num;
                        if (solve(board, i, j + 1))
                            return true;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
        return true;
    }

    public boolean isValid(char[][] board, int row, int col, char c){
        int squareRow = (row / 3) * 3;
        int squareCol = (col / 3) * 3;
        for(int i = 0; i < 9; i++) {
            if(board[i][col] == c || board[row][i] == c || board[squareRow + i / 3][squareCol + i % 3] == c) {
                return false; 
            } 
        }
        return true;
    }
}
        
