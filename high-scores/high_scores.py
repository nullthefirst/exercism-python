def latest(scores):
    return scores[len(scores) - 1]


def personal_best(scores):
    highest = 0
    for x in scores:
        if x > highest:
            highest = x
        else:
            pass
    return highest


def personal_top_three(raw_scores):
    scores = raw_scores.copy()
    top_three = []

    if len(raw_scores) == 1:
        first_best = personal_best(scores)
        top_three.append(first_best)
        scores.remove(first_best)
    else:
        first_best = personal_best(scores)
        top_three.append(first_best)
        scores.remove(first_best)

        second_best = personal_best(scores)
        top_three.append(second_best)
        scores.remove(second_best)

        if len(raw_scores) >= 3:
            third_best = personal_best(scores)
            top_three.append(third_best)
            scores.remove(third_best)
        else:
            pass

    return top_three
