__author__ = 'Andy'


def levenshteinDist(s, len_s, t, len_t):
    dist = 0
    if len_s is 0: return len_t
    if len_t is 0: return len_s

    if (s[len_s - 1] != t[len_t - 1]):
        dist = 1

    return min(levenshteinDist(s, len_s - 1, t, len_t) + 1, \
               levenshteinDist(s, len_s, t, len_t - 1) + 1, \
               levenshteinDist(s, len_s - 1, t, len_t - 1) + dist)


string1 = "beneficial"
string2 = "benefactor"

print(levenshteinDist(string1, len(string1), string2, len(string2)))