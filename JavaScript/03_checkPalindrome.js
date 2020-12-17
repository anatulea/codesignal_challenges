// Given the string, check if it is a palindrome.

// Example

// For inputString = "aabaa", the output should be
// checkPalindrome(inputString) = true;
// For inputString = "abac", the output should be
// checkPalindrome(inputString) = false;
// For inputString = "a", the output should be
// checkPalindrome(inputString) = true.

function checkPalindrome(inputString) {
    const reversed = []
    for(let i = inputString.length-1; i>=0; i--){
        reversed.push(inputString[i])
    }
    return reversed.join('')== inputString
}

function checkPalindrome2(inputString) {
    return inputString == inputString.split('').reverse().join('');
}

function checkPalindrome3(inputString) {
    return [...inputString].reverse().join('') === inputString
}