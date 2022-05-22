s = "anagram"
t = "nagaram"


def anagramCheck(s, t):
    s_len = len(s)
    if (len(t) != s_len):
        return False
    t_dict, s_dict = {}, {}

    for i in range(s_len):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
    for e in s_dict:
        if s_dict[e] != t_dict.get(e, 0):
            return False

    return True
