function adjacentElementsProduct(inputArray) {
    let max_adj = inputArray[0]* inputArray[1]
    
    for(let i = 1; i< inputArray.length-1; i++){
        if (inputArray[i]* inputArray[i+1] > max_adj){
            max_adj = inputArray[i]* inputArray[i+1]
        }
    }
    return max_adj
    }
    