class Solution(object):
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if s == "" or t == "":
      return ""
    ls = len(s)
    t_dic = {}
    for c in t:
      if c not in t_dic:
        t_dic[c] = 1
      else:
        t_dic[c] += 1
    t_set = set(t_dic.keys())
    winh, wint = None, None
    head = 0
    tail = 0
    while tail < ls:
      c = s[tail]
      if c in t_dic:
        t_dic[c] -= 1
        if t_dic[c] == 0:
          t_set.remove(c)
      if not t_set:
        if winh is None:
          winh, wint = head, tail + 1
        elif tail - head + 1 < wint - winh:
          winh, wint = head, tail + 1
        while head <= tail:
          c = s[head]
          if c in t_dic:
            t_dic[c] += 1
            if t_dic[c] == 1:
              if tail - head + 1 < wint - winh:
                winh, wint = head, tail + 1
              t_set.add(c)
              head += 1
              break
          head += 1
      tail += 1
    if winh is None:
      return ""
    else:
      return s[winh: wint]

if __name__ == "__main__":
  sol = Solution()
  print sol.minWindow("bdab", "ab")
