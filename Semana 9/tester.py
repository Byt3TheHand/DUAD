def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = get_average_score(juan_scores)
sofia_scores["average_score"] = get_average_score(sofia_scores)
paul_scores["average_score"] = get_average_score(paul_scores)

juan_scores["is_exempted"] = is_student_exempted(juan_scores)
sofia_scores["is_exempted"] = is_student_exempted(sofia_scores)
paul_scores["is_exempted"] = is_student_exempted(paul_scores)

print(sofia_scores["is_exempted"])