class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    record = [[-1] * len(word2) for _ in range(len(word1))]
    def convert(word1, word2, indword1, indword2):
      if word1 == "" or word2 == "":
        return len(word1 + word2)
      elif record[indword1][indword2] != -1:
        return record[indword1][indword2]
      else:
        if word1[0] == word2[0]:
          record[indword1][indword2] = convert(word1[1:], word2[1:], indword1 + 1, indword2 + 1)
        else:
          # delete op
          delete_steps = convert(word1[1:], word2, indword1 + 1, indword2)

          # insert op
          insert_steps = convert(word1, word2[1:], indword1, indword2 + 1)

          # replace op
          replace_steps = convert(word1[1:], word2[1:], indword1 + 1, indword2 + 1)

          record[indword1][indword2] = min([delete_steps, insert_steps, replace_steps]) + 1

        return record[indword1][indword2]

    return convert(word1, word2, 0, 0)

if __name__ == "__main__":
  sol = Solution()
  print sol.minDistance("dinitrophenylhydrazine","acetylphenylhydrazine")