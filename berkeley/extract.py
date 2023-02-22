f = [a.split()[-1][:-4] for a in open("random_numbers.txt","r").read().split('\n')[:-1]]
print(f)
