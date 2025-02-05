n = int(input())
n_separated_no = list(map(int, input().strip().split()))
fliped_column = " ".join(map(str, sorted(n_separated_no)))
print(fliped_column)
