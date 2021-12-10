from aocd import get_data

input = get_data(year=2021,day=10).split("\n")

syntax_error_scores = {")":3, "]":57, "}":1197, ">":25137}
autocomplete_scores = {"(":1, "[":2, "{":3, "<":4}
pairs = ["()", "{}", "[]", "<>"]
opening = [p[0] for p in pairs]
closing = [p[1] for p in pairs]

def get_error_score(line):
    stack = []

    for c in list(line):
        valid = False
        if(c in opening):
            stack.append(c)
            valid = True

        elif(c in closing):

            if (stack[-1] in opening and closing.index(c) == opening.index(stack[-1])):
                stack.pop(-1)
                valid = True

        if not valid:
            return [syntax_error_scores[c], list(reversed(stack))]

    return [0, list(reversed(stack))]


def get_autocomplete_score(reversed_stack):
    score = 0

    for c in reversed_stack:
        score *= 5
        score += autocomplete_scores[c]

    return score

autocomplete_scores_list = []

for line in input:
    result = get_error_score(line)

    if(result[0] == 0):
        autocomplete_scores_list.append(get_autocomplete_score(result[1]))

autocomplete_scores_list.sort()
print(autocomplete_scores_list[len(autocomplete_scores_list) // 2])
