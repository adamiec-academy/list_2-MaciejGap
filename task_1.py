def remove_parentheses(text):
    result = ""
    is_inside = False
    i = 0
    while i < len(text):
        if text[i] == "(":
            is_inside = True
        elif text[i] == ")":
            is_inside = False
            i = i + 1
        elif not is_inside:
            result = result + text[i]

        i = i + 1
    return result
