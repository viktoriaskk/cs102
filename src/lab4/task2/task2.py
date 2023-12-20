import sys

class AgeGroupBreakdown:
    def __init__(self, age_groups):
        self.age_groups = age_groups
        self.respondents = []

    def add_respondent(self, name, age):
        self.respondents.append((name, age))

    def get_age_group_breakdown(self):
        age_group_breakdown = []

        # Sort respondents by age in descending order
        self.respondents.sort(key=lambda x: x[1], reverse=True)

        for age_group in self.age_groups:
            group_name = self.get_age_group_name(age_group)
            group_respondents = []

            for respondent in self.respondents:
                name, age = respondent
                if self.is_in_age_group(age, age_group):
                    group_respondents.append(f"{name} ({age})")

            if group_respondents:
                age_group_breakdown.append(f"{group_name}: {', '.join(group_respondents)}")

        return age_group_breakdown

    @staticmethod
    def get_age_group_name(age_group):
        if age_group[1] == 123:
            return f"{age_group[0]}+"
        else:
            return f"{age_group[0]}-{age_group[1]}"

    @staticmethod
    def is_in_age_group(age, age_group):
        return age_group[0] <= age <= age_group[1]


def main():
    age_group_args = sys.argv[1:]

    age_groups = [(int(age_group_args[i]), int(age_group_args[i + 1])) for i in range(0, len(age_group_args)-1, 2)]
    age_groups.append((int(age_group_args[-1]), 123))
    print(age_groups)
    age_group_breakdown = AgeGroupBreakdown(age_groups)

    for line in sys.stdin:
        if line.strip() == "END":
            break
        name, age = line.strip().split(",")
        age_group_breakdown.add_respondent(name, int(age))

    breakdown = age_group_breakdown.get_age_group_breakdown()

    for group in breakdown:
        print(group)


if __name__ == "__main__":
    main()
