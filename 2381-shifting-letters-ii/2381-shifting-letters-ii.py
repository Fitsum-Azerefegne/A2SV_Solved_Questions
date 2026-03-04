class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_arr = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                shift_arr[start] += 1
                shift_arr[end + 1] -= 1
            else:
                shift_arr[start] -= 1
                shift_arr[end + 1] += 1
        shifted = []
        current_shift = 0
        for i in range(len(s)):
            current_shift += shift_arr[i]
            original_char = s[i]
            shifted_char = chr((ord(original_char) - ord('a') + current_shift) % 26 + ord('a'))
            shifted.append(shifted_char)
        
        return ''.join(shifted)