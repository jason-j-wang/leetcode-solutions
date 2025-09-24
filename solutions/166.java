//https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=daily-question&envId=2025-09-24
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {

        if (numerator % denominator == 0) {
            return Long.toString((long) numerator/(long) denominator);
        }

        StringBuilder ans = new StringBuilder();
        Map<Long, Integer> seen = new HashMap<>();
        
        long denom = Math.abs((long) denominator);
        long num = Math.abs((long) numerator) % denom;
        int i = 0;
        
        while (num != 0) {
            num *= 10;
            int decimal = (int) (num / denom);

            if (seen.containsKey(num)) {
                int index = seen.get(num);
                ans.insert(index, "(");
                ans.append(")");
                break;
            }

            
            seen.put(num, i);
            ans.append(Integer.toString(decimal));
            
            num = num % denom;
            i++;
        }

        ans.insert(0, ".");
        ans.insert(0, Long.toString(Math.abs((long) numerator)/denom));

        if ((numerator  < 0) ^ (denominator < 0)) {
            ans.insert(0, "-");
        }
        return ans.toString();
    }
}