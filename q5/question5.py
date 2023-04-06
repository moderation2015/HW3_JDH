def reverse_words():
    s1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    s2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    s1list = s1.split()
    s1list.reverse()
    ans1 = ""
    for i in s1list:
        ans1 = ans1 + i
        ans1 = ans1 + " "
    ans1 = ans1.rstrip()
    print("*** string1 is ***")
    print(s1)
    print("*** string1 reverse is ***")
    print(ans1)

    s2list = s2.split()
    s2list.reverse()
    ans2 = ""
    for i in s2list:
        ans2 = ans2 + i
        ans2 = ans2 + " "
    ans2 = ans2.rstrip()
    print()
    print("*** string2 is ***")
    print(s2)
    print("*** string2 reverse is ***")
    print(ans2)


def main():
    reverse_words()

if __name__ == "__main__":
    main()




