class CrewMember:
    retirement_age = 70

print(CrewMember.retirement_age)

kirk = CrewMember()

print(kirk.retirement_age)
CrewMember.retirement_age = 65
CrewMember = CrewMember()
CrewMember.retirement_age = 50
print(CrewMember.retirement_age)
print(kirk.retirement_age)