/*After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9. */
function matrixElementsSum(matrix) {
    let total= 0;
    for (let row = 0; row< matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] === 0 ) {
                for (let i = 0; i < matrix.length - row; i++) {
                    matrix[row+i][col] = 0; // changing to zero all the numbers under a zero
                }
            }else {
                total += matrix[row][col]
            }
        }
    } 
    return total
}


function matrixElementsSum2(matrix) {
    for(var r=0,j=0;j<matrix[0].length;j++){
        for(var i=0;i<matrix.length;i++){
          if(matrix[i][j]===0) break
          else r+=matrix[i][j]
        }
    }
    return r
  }
  