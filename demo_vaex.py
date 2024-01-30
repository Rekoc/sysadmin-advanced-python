import vaex
import os, pathlib


def is_even(value) -> bool:
        return True if value % 2 == 0 else False

def add_values(val1, val2) -> int | float:
    return val1 + val2


def main():
    root_file = pathlib.Path(__file__).parent.resolve()
    csv_path = os.path.join(root_file, "statics", "excel_file.csv")

    df = vaex.read_csv(csv_path)
    print(df)

    # Sélection des lignes répondant à la query
    df.select(df.gains < 0)
    # Stockage des lignes sélectionnées dans 'rows'
    rows = df.evaluate(df.clientid, selection=True)
    print(rows) # [0 2 3 5 8 9]

    # Query simple retournant les lignes qui match
    df_gains_negative = df[df.gains < 0]
    print(df_gains_negative)
    #   #    clientid  date        weekdays      gains    prices  up
    #   0           0  2008-04-30  Wed              -5       7.3  False
    #   1           2  2008-05-02  Fri              -2       9    False
    #   2           3  2008-05-03  Sat              -4       8    False
    #   3           5  2008-05-05  Mon              -2      12.7  False
    #   4           8  2008-05-08  Thu              -1      19    False
    #   5           9  2008-05-09  Fri              -1       8    False


    df["new_col"] = df.gains ** 2
    print(df)
    #   #    clientid  date        weekdays      gains    prices  up       new_col
    #   0           0  2008-04-30  Wed              -5      7.3   False         25
    #   1           1  2008-05-01  Thu               1      3.3   True           1
    #   2           2  2008-05-02  Fri              -2      9     False          4
    #   3           3  2008-05-03  Sat              -4      8     False         16
    #   4           4  2008-05-04  Sun               0      9.4   True           0
    #   5           5  2008-05-05  Mon              -2     12.7   False          4
    #   6           6  2008-05-06  Tue               0      7.1   True           0
    #   7           7  2008-05-07  Wed               2      7.67  True           4
    #   8           8  2008-05-08  Thu              -1     19     False          1
    #   9           9  2008-05-09  Fri              -1      8     False          1

    print(df.new_col.sum())
    # 56

    # OK
    df["is_even"] = df.apply(is_even, arguments=[df.prices])
    print(df)

    # NOK
    df["sum"] = df.apply(add_values, arguments=[df.gains, df.prices])
    print(df)
    # A la place
    df["sum"] = df.gains + df.prices
    #   #    clientid  date        weekdays      gains    prices  up       new_col  is_even      sum
    #   0           0  2008-04-30  Wed              -5      7.3   False         25  False       2.3
    #   1           1  2008-05-01  Thu               1      3.3   True           1  False       4.3
    #   2           2  2008-05-02  Fri              -2      9     False          4  False       7
    #   3           3  2008-05-03  Sat              -4      8     False         16  True        4
    #   4           4  2008-05-04  Sun               0      9.4   True           0  False       9.4
    #   5           5  2008-05-05  Mon              -2     12.7   False          4  False      10.7
    #   6           6  2008-05-06  Tue               0      7.1   True           0  False       7.1
    #   7           7  2008-05-07  Wed               2      7.67  True           4  False       9.67
    #   8           8  2008-05-08  Thu              -1     19     False          1  False      18
    #   9           9  2008-05-09  Fri              -1      8     False          1  True        7

    # Premiere query
    dff = df[df.gains < 0]
    print(dff)
    # Deuxième ('filter()' fait la même chose qu'une query classique)
    dff1 = dff.filter(dff.prices > 9)
    print(dff1)
    #   #    clientid  date        weekdays      gains    prices  up       new_col  is_even      sum
    #   0           5  2008-05-05  Mon              -2      12.7  False          4  False       10.7
    #   1           8  2008-05-08  Thu              -1      19    False          1  False       18

    dff2 = dff.filter(dff.prices > 9, mode="or")
    print(dff2)
    #  #    clientid  date        weekdays      gains    prices  up       new_col  is_even      sum
    #   0           0  2008-04-30  Wed              -5       7.3  False         25  False        2.3
    #   1           2  2008-05-02  Fri              -2       9    False          4  False        7
    #   2           3  2008-05-03  Sat              -4       8    False         16  True         4
    #   3           4  2008-05-04  Sun               0       9.4  True           0  False        9.4
    #   4           5  2008-05-05  Mon              -2      12.7  False          4  False       10.7
    #   5           8  2008-05-08  Thu              -1      19    False          1  False       18
    #   6           9  2008-05-09  Fri              -1       8    False          1  True         7


if __name__ == '__main__':
    main()