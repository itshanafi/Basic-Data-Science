# Logical operator is to solve more than one condition
# and : both/all condition must be true
# or : at least one condition must be true
# not : negate the condition

x = 4
y = 10
z = 14

print(x > y and x > z)
print(y < x or y > z)

# sometime some statement to be executed when the condition fails
# but do not have any statement to be executed when the condition is true.
print(not z)