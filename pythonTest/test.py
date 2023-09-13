# True
# False
# True
# True
# False

def is_palindrome(word):
    for i in range(len(word) // 2):
        if(word[i] != word[-i-1]):
            return False;
    return True;

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))