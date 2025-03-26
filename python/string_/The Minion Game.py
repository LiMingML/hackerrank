def minion_game(string):
    # your code goes here
    vow = set("AEIOU")
    stuart_score = 0
    kevin_score = 0

    for i in range(len(string)):
        if string[i] in vow:
            # import rules
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if stuart_score > kevin_score:
        print(f"Stuart {kevin_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)