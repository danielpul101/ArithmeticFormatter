def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    prob_info = []
    for item in problems:
        temp = []
        temp.extend(item.split(' '))
        prob_info.append(temp)

    for x in prob_info:
        if x[1] != '+' and x[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not x[0].isnumeric() or not x[2].isnumeric():
            return 'Error: Numbers must only contain digits.'
        if len(x[0]) > 4 or len(x[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if len(x[0]) > len(x[2]):
            spaces = len(x[0]) - len(x[2])
            for i in range(spaces):
                x[2] = " " + x[2]

        else:
            spaces = len(x[2]) - len(x[0])
            for i in range(spaces):
                x[0] = " " + x[0]

    ans_list = []
    for item in problems:
        temp_list = []
        temp_list.append(eval(item))
        temp_list.append(item.split(' '))
        ans_list.append(temp_list)


    problems = ''
    for x in prob_info:
        problems += f'  {x[0]}    '
    problems = problems[:-4]
    problems += '\n'

    for x in prob_info:
        problems += f'{x[1]} {x[2]}    '
    problems = problems[:-4]
    problems += '\n'

    for x in prob_info:
        for y in range(len(x[0])+2):
            problems += '-'
        problems += '    '
    problems = problems[:-4]

    if show_answers:
        problems += '\n'
        for x in ans_list:
            if len(str(x[0])) > len(x[1][2]) and len(str(x[0])) > len(x[1][0]):
                problems += f' {x[0]}    '

            elif len(str(x[0])) < len(x[1][2]) and len(str(x[0])) < len(x[1][0]):
                problems += f'  {x[0]}    '

            else:
                problems += f'  {x[0]}    '

        problems = problems[:-4]

    return problems