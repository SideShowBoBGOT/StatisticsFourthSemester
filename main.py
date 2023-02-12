from my_statistic_values import *
from my_distributions import *

# formulas fot homework 5-6





intervals = [
    (0, 5, 30),
    (5, 10, 16),
    (10, 15, 7),
    (15, 20, 3),
    (20, 25, 2),
    (25, 30, 1),
    (30, 35, 1)
]
arg_func = lambda x: 1 - math.pow(math.e, -0.14 * x)

print(kolmogorov_smirnov(intervals, arg_func))

# s_one = '75 85 84 81 84 80 82 76 75 77 ' \
#         '80 82 81 84 85 77 76 84 83 84 ' \
#         '78 77 88 86 87 79 80 79 78 87 ' \
#         '78 77 88 86 84 79 80 79 78 81'
#
# s_two = '12 14 19 15 14 18 13 16 17 12 ' \
#         '20 17 15 13 17 16 20 14 14 13 ' \
#         '17 16 15 19 16 15 18 17 15 14 ' \
#         '16 15 15 18 15 15 19 14 16 18 ' \
#         '18 15 15 17 15 16 16 14 14 17'

# confidence_level = 0.05
# nums_one = float_sequence_from_str(s_one)
# nums_two = float_sequence_from_str(s_two)
# print(f'1) {is_dispersions_equal(nums_one, nums_two, confidence_level)}')
# print(f'2) {is_mathematical_expectation_equals_value(nums_two, 15, confidence_level)}')
# print(f'3) a) {is_mathematical_expectations_equal_independent(nums_one, nums_two, confidence_level)}')
# print(f'3) b) {is_mathematical_expectations_equal_dependent(nums_one, nums_two, confidence_level)}')
# print(f'4) {is_sequences_independent(nums_one, nums_two, confidence_level)}')
# print(f'5) a {is_sample_dispersion_equal_to_general_reverse_greater(nums_one, 0.12, confidence_level)}')
# print(f'5) b {is_sample_dispersion_equal_to_general_reverse_not_equal(nums_one, 0.12, confidence_level)}')
# print(f'5) c {is_sample_dispersion_equal_to_general_reverse_smaller(nums_one, 0.12, confidence_level)}')

# intervals = interval_sequence(nums_count_freq)
# print_interval_sequence(intervals)
# discrete = discrete_sequence_from_interval(intervals)
# cumulate_ogiva(discrete)

# total_elements = len(nums)
# xb = x_b(nums)
# s2 = s_squared(nums)

# print(f'prob_pairs: {pairs_prob}')
# print(f'xb: {xb}')
# print(f's2: {s2}')
