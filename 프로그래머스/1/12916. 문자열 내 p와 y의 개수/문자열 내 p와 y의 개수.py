def solution(s):
    countp = 0
    county = 0
    for word in s:
        if word == "p" or word == "P":
            countp += 1
        elif word == "y" or word == "Y":
            county += 1

    return countp == county