def generate_match_summary(team1, team2, score):
    return f"""
MATCH SUMMARY

{team1} {score} {team2}

The match delivered plenty of excitement from start to finish.
Both teams created chances, but the final score tells the story.

Who was your Man of the Match?
Comment below.
"""

if __name__ == "__main__":
    print(generate_match_summary("Manchester City", "Arsenal", "3-1"))
