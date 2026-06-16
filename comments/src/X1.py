class Maths:

    @staticmethod
    def sum_squares_of_range(lower_bound, upper_bound):
        accumulated_sum = 0

        for i in range(lower_bound, upper_bound + 1):
            accumulated_sum += Maths.square(i)

        return accumulated_sum

    @staticmethod
    def square(k):
        return k * k
