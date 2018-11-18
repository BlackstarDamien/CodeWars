import re
class Calculator(object):
  def evaluate(self, string):
    operators = {"-": lambda x,y: x-y, "+": lambda x,y: x+y, "*": lambda x,y: x*y, "/": lambda x,y: x/y}
    operator_order = ('/*', '+-')
    ops = [i for i in re.findall("[/|*|+|-]",string)]
    #nums = [float(i) for i in string if i.isdigit()]
    nums = [float(i) for i in re.findall("[-+]?\d*\.\d+|\d+",string)]
    val = None
    for op in operator_order:
        while any(o in ops for o in op):
            idx,oo = next((i,o) for i,o in enumerate(ops) if o in op)
            ops.pop(idx)
            vals = map(float,nums[idx:idx+2])
            val = operators[oo](*vals)
            nums[idx:idx+2] = [val]
    if isinstance(nums[0],float):
        return nums[0]
    else:
        return int(nums[0])
