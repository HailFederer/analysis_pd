import pandas as pd


# price = [92600, 92400, 92100, 94300, 92300]
# s = pd.Series(price)
# print(s)
# print(s[0], s[1])


# s = pd.Series(
#     [92600, 92400, 92100, 94300, 92300],
#     index=['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-05-05'])
# print(s)
# print(s[1], s['2017-02-02'])


# s = pd.Series(7, index=['a', 'b', 'c', 'd'])
# print(s)


# for date in s.index:
#     print(date, end=' ')
# else:
#     print()
#
# for price in s.values:
#     print(price, end=' ')
# else:
#     print()


# d = {'a': 10, 'b': 20, 'c': 30}
# s = pd.Series(d)
# print(s)
#
# s = pd.Series(d, index=['a', 'b', 'c', 'd'])
# print(s)

df1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],  'value': range(6)})
df1 = df1.set_index('key')
print(df1)
df2 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(df2)
print(pd.merge(df1, df2, left_index=True, right_index=True))


