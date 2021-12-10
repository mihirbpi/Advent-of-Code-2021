from aocd import get_data

input = get_data(year=2021,day=10).split("\n")

scores = {")":3, "]":57, "}":1197, ">":25137}
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
            top = stack[-1]

            if (top in opening and closing.index(c) == opening.index(top)):
                stack.pop()
                valid = True

        if not valid:
            return scores[c]

    return 0

print(sum([get_error_score(line) for line in input]))
