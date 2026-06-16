class X1:

    @staticmethod
    def sum_squares_of_range(q, z):
        accumulated_sum = 0

        # Iterate from lower bound (q) to upper bound (z)
        for i in range(q, z + 1):
            # Add square of each number in the range
            accumulated_sum += X1.square(i)

        return accumulated_sum

    @staticmethod
    def square(k):
        return k * k