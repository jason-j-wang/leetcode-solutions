//https://leetcode.com/problems/valid-sudoku/description/?envType=daily-question&envId=2025-08-30
class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = 9;

        for (int i = 0; i < n; i++) {
            Set<Character> row_seen = new HashSet<>();
            Set<Character> col_seen = new HashSet<>();

            for (int j = 0; j < n; j++) {
                if (board[i][j] != '.' && row_seen.contains(board[i][j])) {
                    return false;
                }
                row_seen.add(board[i][j]);

                if (board[j][i] != '.' && col_seen.contains(board[j][i])) {
                    return false;
                }
                col_seen.add(board[j][i]);

            }
        }

        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                Set<Character> seen = new HashSet<>();
                for (int i = 3 * a; i < 3 * a + 3; i++) {
                    for (int j = 3 * b; j < 3 * b + 3; j++) {
                        if (board[i][j] != '.' && seen.contains(board[i][j])) {
                            return false;
                        }
                        seen.add(board[i][j]);
                    }
                }
            }
        }
        return true;
    }
}