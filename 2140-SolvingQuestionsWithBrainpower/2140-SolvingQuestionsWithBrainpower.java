// Last updated: 3/31/2025, 7:38:05 PM
class Solution {
    public long mostPoints(int[][] questions) {
        return _mostPoints(questions, 0, new HashMap<>());
    }

    public long _mostPoints(int[][] questions, int idx, Map<Integer, Long> memo) {
        if(questions.length <= idx) {
            return 0;
        }
        if(memo.containsKey(idx)) {
            return memo.get(idx);
        }

        long res = Math.max(
            _mostPoints(questions, idx + questions[idx][1] + 1, memo) + questions[idx][0],
            _mostPoints(questions, idx + 1, memo)
        );

        memo.put(idx, res);
        return res;
    }
}