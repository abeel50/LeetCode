class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        next_greatest_letter_index = float('inf')
        for i, l in enumerate(letters):
            if target < l and i < next_greatest_letter_index:
                next_greatest_letter_index = i
        if next_greatest_letter_index != float('inf'):
            return letters[next_greatest_letter_index]
        return min(letters)
            
