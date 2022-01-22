class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # create frequency map in pattern
        char_frequency = {}
        for char in s1:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

        window_start = 0
        matched = 0
        for window_end in range(len(s2)):
            # add char to the window
            current_char = s2[window_end]

            # if current character in the frequency map
            if current_char in char_frequency:
                # decrement the frequency
                char_frequency[current_char] -= 1
                # if frequency is 0,we have a complete match of one character within the window
                # increased the matched distinct character count
                if char_frequency[current_char] == 0:
                    matched += 1
            # if any point,matched distinct character count equal to length of freq map
            # we found a permutaton,return true
            if matched == len(char_frequency):
                return True

            # if window end is greater than the length of the pattern
            # remove characters from begining of the window
            if window_end >= len(s1) - 1:
                remove_char = s2[window_start]
                # if the character to be remove was in part of the freq map
                if remove_char in char_frequency:
                    # and the character freq was 0,since we are removing character from window matched count
                    # decrement by one
                    if char_frequency[remove_char] == 0:
                        matched -= 1
                    # since we are removing from the window,freqency count should increment
                    char_frequency[remove_char] += 1
                window_start += 1
        return False
