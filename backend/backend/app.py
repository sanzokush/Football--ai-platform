from football_data import get_live_matches
from content_generator import generate_post

def run():
    match = get_live_matches()

    print("Football AI Platform")
    print(match)

    sample_post = generate_post(
        "Manchester City",
        "Arsenal",
        "3-1"
    )

    print(sample_post)

if __name__ == "__main__":
    run()
