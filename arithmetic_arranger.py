def arithmetic_arranger(problems, display=False):
  arranged_problems = None

  if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
  
  calculus_op = [op.split()[1] for op in problems]
  
  for op in calculus_op:
    if op not in ['+', '-']:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
  
  numeric_operands = []
  for item in problems:
    oper1, _ , oper2 = item.split()
    numeric_operands.extend([oper1, oper2])

  
  for item in numeric_operands:
    if not item.isdigit():
      arranged_problems = 'Error: Numbers must only contain digits.'
      return arranged_problems
  
    if len(item) > 4:
      arranged_problems = 'Error: Numbers cannot be more than four digits.'
      return arranged_problems
  
  top_operands_row, bottom_dashes, result = '', '', ''
  
  for item in range(0, len(numeric_operands), 2):
    space = max(len(numeric_operands[item]), len(numeric_operands[item+1])) + 2
    top_operands_row = top_operands_row + numeric_operands[item].rjust(space)
    bottom_dashes = bottom_dashes + ('-' * space)
    result = result + str([eval(x) for x in problems][item//2]).rjust(space)

    if item != len(numeric_operands) - 2:
            top_operands_row = top_operands_row + (' ' * 4)
            bottom_dashes = bottom_dashes + (' ' * 4)
            result = result + (' ' * 4)
  
  bottom_operands_row = ''
  for item in range(1, len(numeric_operands), 2):
    space = max(len(numeric_operands[item-1]), len(numeric_operands[item])) + 1
    bottom_operands_row = bottom_operands_row + calculus_op[item//2]
    bottom_operands_row = bottom_operands_row + numeric_operands[item].rjust(space)

    if item != len(numeric_operands) - 1:
      bottom_operands_row = bottom_operands_row + (' ' * 4)

  arranged_problems = '\n'.join((top_operands_row, bottom_operands_row, bottom_dashes)) 

  if display:
    arranged_problems = '\n'.join((top_operands_row, bottom_operands_row, bottom_dashes, result)) 
    return arranged_problems
  
  return arranged_problems