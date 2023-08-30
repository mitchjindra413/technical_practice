class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        return String(String(x).reversed()) == String(x)
    }
}