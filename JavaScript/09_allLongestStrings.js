/*Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

 */

function allLongestStrings(inputArray) {
    let max_len = 0;
    let allStr = [];
    for(let i = 0; i<inputArray.length; i++) {
        if (inputArray[i].length > max_len) {
            max_len = inputArray[i].length
        }
    }
    for(let i = 0; i<inputArray.length; i++) {
        if (inputArray[i].length === max_len) {
            allStr.push(inputArray[i])
        }
    }
    return allStr
}

function allLongestStrings2(inputArray) {
    'use strict';
    let maxSize = Math.max(...inputArray.map(x => x.length));
    return inputArray.filter(x => x.length === maxSize);
}
function allLongestStrings3(inputArray) {
    return inputArray.filter(x => x.length === Math.max(...inputArray.map(x => x.length)));}