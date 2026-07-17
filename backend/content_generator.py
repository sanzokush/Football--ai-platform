def generate_post(team1, team2, score):
    return f"""⚽ FULL TIME

{team1} {score} {team2}

Who impressed you the most?

👇 Drop your thoughts in the comments.
"""

if __name__ == "__main__":
    print(generate_post("Manchester City", "Arsenal", "3-1"))
