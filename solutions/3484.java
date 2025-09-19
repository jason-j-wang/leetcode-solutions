//https://leetcode.com/problems/design-spreadsheet/description/?envType=daily-question&envId=2025-09-19
class Spreadsheet {

    private int[][] sheet;

    public Spreadsheet(int rows) {
        sheet = new int[rows][26];
    }
    
    public void setCell(String cell, int value) {
        char letter = cell.charAt(0);
        int row = Integer.parseInt(cell.substring(1));

        sheet[row - 1][letter - 'A'] = value;
    }
    
    public void resetCell(String cell) {
        char letter = cell.charAt(0);
        int row = Integer.parseInt(cell.substring(1));

        sheet[row - 1][letter - 'A'] = 0;
        
    }
    
    public int getValue(String formula) {
        String[] parsed = formula.substring(1).split("\\+");

        int left = 0;
        int right = 0;

        if (isNumber(parsed[0].charAt(0))) {
            left = Integer.parseInt(parsed[0]);
        } else {
            char letter = parsed[0].charAt(0);
            int row = Integer.parseInt(parsed[0].substring(1));

            left = sheet[row - 1][letter - 'A'];
        }

        if (isNumber(parsed[1].charAt(0))) {
            right = Integer.parseInt(parsed[1]);
        } else {
            char letter = parsed[1].charAt(0);
            int row = Integer.parseInt(parsed[1].substring(1));

            right = sheet[row - 1][letter - 'A'];
        }

        return left + right;
    }

    private boolean isNumber(char c) {
        return Character.isDigit(c);
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */