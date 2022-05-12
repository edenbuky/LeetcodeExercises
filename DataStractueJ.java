import java.util.HashSet;

public class DataStractueJ {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0 ; i < m ; i++){
            if ( matrix[i][0] <= target && matrix[i][n-1] >= target){
                for ( int j=0 ; j < n ; j++){
                    if (matrix[i][j] == target) return true;
                }
            }
        }
        return false;
    }
    public boolean isValidSudoku(char[][] board) {

        HashSet<String> seen = new HashSet();
        for (int i=0 ; i < 9 ; i++){
            for (int j=0 ; j < 9; j++){
                char curr = board[i][j];
                if (curr != '.'){
                    if (!seen.add(curr + " row " + i) ||
                            !seen.add(curr + " column "+ j )||
                            !seen.add(curr + " box " + i/3 + "X"+ j/3)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
