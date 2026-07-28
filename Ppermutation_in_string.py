class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        count_s1 = {}
        count_s2_wind = {}
        for i in range(n1):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1
            count_s2_wind[s2[i]] = count_s2_wind.get(s2[i], 0) + 1
        if count_s1 == count_s2_wind:
            return True
        for right in range(n1, n2):
            c_in = s2[right]
            count_s2_wind[c_in] = count_s2_wind.get(c_in, 0) + 1

            c_out = s2[right-n1]
            count_s2_wind[c_out] = count_s2_wind.get(c_out, 0) - 1

            if count_s2_wind[c_out] == 0:
                del count_s2_wind[c_out]
            if count_s1 == count_s2_wind:
                return True
        return False
                


