class Solution(object):
  def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    path_stack = ["/"]
    ind = 0
    while ind < len(path):
      if path[ind] != "/":
        break
      ind += 1
    record = ""
    new_path = path[ind:]
    for c in new_path:
      if c == "/":
        if record == "." or record == "":
          pass
        elif record == "..":
          if len(path_stack) > 1:
            path_stack.pop()
        else:
          path_stack.append(record)
        record = ""
      else:
        record += c
    if record == "." or record == "":
      pass
    elif record == "..":
      if len(path_stack) > 1:
        path_stack.pop()
    else:
      path_stack.append(record)

    return path_stack[0] + "/".join(path_stack[1:])