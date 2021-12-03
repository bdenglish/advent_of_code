from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN

import pandas as pd

import common

lines = common.read_input_lines_to_list(2021, 3)
# lines = ['00100', '11110', '10110', '10111', '10101', '01111',
#          '00111', '11100', '10000', '11001', '00010', '01010']


def get_most_common_bits(_df, round_method=ROUND_HALF_UP):
    _df = _df.astype(int)
    means = _df.mean()
    return means.apply(lambda x: str(int(Decimal(x).quantize(0, round_method))))


df = pd.DataFrame([list(line) for line in lines])
# df = df.astype(int)
# most_common_bit = round(df.mean(), 0).astype(int).astype(str)
most_common_bits = get_most_common_bits(df)
df = df.astype(str)
gamma_str = ''.join(most_common_bits.tolist())
gamma_dec = int(gamma_str, 2)
print(gamma_dec)
epsilon = ''.join(["0" if n == "1" else "1" for n in gamma_str])
epsilon_bin = int(epsilon, 2)
print(epsilon_bin)

print(gamma_dec * epsilon_bin)

oxygen = df.copy(deep=True)
for col in df.columns:
    oxygen = oxygen.loc[oxygen[col] == get_most_common_bits(oxygen)[col]]
    if len(oxygen) == 1:
        oxygen_rating = int(''.join(oxygen.values.tolist()[0]), 2)
        break

print(oxygen_rating)

co2 = df.copy(deep=True)
for col in df.columns:
    least_common_bits = get_most_common_bits(co2, ROUND_HALF_UP).values.tolist()
    least_common_bit = "0" if least_common_bits[col] == "1" else "1"
    co2 = co2.loc[co2[col] == least_common_bit]
    if len(co2) == 1:
        co2_rating = int(''.join(co2.values.tolist()[0]), 2)
        break

print(co2_rating)

print(oxygen_rating * co2_rating)