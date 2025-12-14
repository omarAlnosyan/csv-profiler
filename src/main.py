from csv_profiler.io import read_csv
from csv_profiler.profile import profile_data
from csv_profiler.render import write_json, write_markdown

def main():
    data = read_csv("data/sample.csv")
    profile = profile_data(data)
    write_json(profile, "output/sample_profile.json")
    write_markdown(profile, "output/sample_profile.md")

if __name__ == "__main__":
    main()