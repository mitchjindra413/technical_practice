class Solution {
    public record Cords(int r, int c) {
        public ArrayList<Integer> toArrayList() {
            ArrayList<Integer> res = new ArrayList<>(List.of(r,c));
            return res;
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        
        int rows = heights.length;
        int cols = heights[0].length;

        Set<Cords> pac = new HashSet<>();
        Set<Cords> atl = new HashSet<>();

        for(int c = 0; c < cols; c++) {
            dfs(heights, 0, c, pac, 0);
            dfs(heights, rows - 1, c, atl, 0);
        }
        for(int r = 0; r < rows; r++) {
            dfs(heights, r, 0, pac, 0);
            dfs(heights, r, cols - 1, atl, 0);
        }
        
        List<List<Integer>> res = new ArrayList<>();
        for(Cords cord : pac) {
            if(atl.contains(cord)) {
                res.add(cord.toArrayList());
            }
        }

        return res;
    }

    public void dfs(int[][] heights, int r, int c, Set<Cords> valid, int prev) {
        Cords key = new Cords(r,c);
        if(valid.contains(key)) {
            return;
        }
        if(r < 0 || r >= heights.length || c < 0 || c >= heights[0].length) {
            return;
        }
        if(heights[r][c] < prev) {
            return;
        }

        valid.add(key);
        
        dfs(heights, r + 1, c, valid, heights[r][c]);
        dfs(heights, r - 1, c, valid, heights[r][c]);
        dfs(heights, r, c + 1, valid, heights[r][c]);
        dfs(heights, r, c - 1, valid, heights[r][c]);
    }
}