# Parse and evaluate simple math word problems returning the answer as an integer.
# What is 5?    -> 5
# What is 5 plus 13?    -> 13
# What is 7 minus 5?    -> 2
# What is 6 multiplied by 4?     -> 24
# What is 25 divided by 5?       -> 5
# What is 5 plus 13 plus 6?      -> 24
# What is 3 plus 2 multiplied by 3?       -> 15

class MathProblemSolver:
    """
    Parse and evaluate simple math word problems returning the answer as an integer.
    """

    def __init__(self):
        pass

    def answer(self, question: str) -> int:
        """
        Parse and evaluate simple math word problems returning the answer as an integer.

        :param question: str - word problem to solve.
        :return: int - numerical solution to the problem.
        """
        if question[:7] != "What is" or question[-1] != "?":
            raise ValueError("unknown operation")
        problem = question[8:-1].split()
        problem = [word for word in problem if word not in ["by"]]
        if len(problem) < 1:
            raise ValueError("syntax error")
        operations = {"plus": lambda x, y: x + y, "minus": lambda x, y: x - y, "multiplied": lambda x, y: x * y, "divided": lambda x, y: x // y}

        def evaluate(problem):
            i = 0
            while i < len(problem):
                if problem[i] in operations:
                    op = operations[problem[i]]
                    left = int(problem[i-1])
                    right = int(problem[i+1])
                    problem = problem[:i-1] + [str(op(left, right))] + problem[i+2:]
                    i -= 1
                i += 1
            return int(problem[0])

        return evaluate(problem)


def main():
    solver = MathProblemSolver()
    print(solver.answer("What is 5?"))
    print(solver.answer("What is 5 plus 13?"))
    print(solver.answer("What is 7 minus 5?"))
    print(solver.answer("What is 6 multiplied by 4?"))
    print(solver.answer("What is 25 divided by 5?"))
    print(solver.answer("What is 5 plus 13 plus 6?"))
    print(solver.answer("What is 3 plus 2 multiplied by 3?"))


if __name__ == '__main__':
    main()