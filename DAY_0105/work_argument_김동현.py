# 30.6
korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

# 30.7

korean, english, mathematics, science = map(int, input('네 과목의 점수를 입력 : ').split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(*args):
    return sum(args) / len(args)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average( korean, english, mathematics, science)
print('낮은 점수 : {0}, 높은 점수 : {1}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average_score))