# coding: utf-8
# create by tongshiwei on 2018/5/1

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        s1_idx = 0
        s2_idx = 0
        s3_idx = 0
        status_stack = []
        while s3_idx < len(s3):
            tag1, tag2 = False, False
            if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
                tag1 = True
            if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                tag2 = True
            if not tag1 and not tag2:
                if not status_stack:
                    return False
                else:
                    s1_idx, s2_idx, s3_idx = status_stack.pop()
            elif tag1 and not tag2:
                s1_idx += 1
                s3_idx += 1
            elif tag2 and not tag1:
                s2_idx += 1
                s3_idx += 1
            else:
                status_stack.append([s1_idx, s2_idx + 1, s3_idx + 1])
                s1_idx += 1
                s3_idx += 1
        return True


if __name__ == '__main__':
    s = Solution()
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print(s.isInterleave(s1, s2, s3))
