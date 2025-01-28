//https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int getMinimumDifference(TreeNode root) {
        ArrayList<Integer> vals = new ArrayList<>();
        dfs(root, vals);
        int ans = Integer.MAX_VALUE;

        for (int i = 1; i < vals.size(); i++) {
            ans = Math.min(ans, Math.abs(vals.get(i) - vals.get(i-1)));
        }
        return ans;
    }

    public ArrayList<Integer> dfs(TreeNode node, ArrayList<Integer> vals) {
        if (node == null) {
            return vals;
        }

        dfs(node.left, vals);
        vals.add(node.val);
        return dfs(node.right, vals);
    }
}