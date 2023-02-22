import math

g = [[1,7],[1,8],[1,9],[1,0],[2,8],[2,9],[2,0],[2,6],[3,7],[3,6],[3,9],[3,0],[4,0],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8],[5,9]]
n = 10
res = 10

def unit(graph,numnodes):


	loc = []
	for x in range(0,n):
		loc.append([0,0])

	box = math.ceil(numnodes/2)

	for x in range(0,20):
		print(x)
		for y in range(0,numnodes):
			score = float('inf')
			bestx = 0
			besty = 0
			for z in range(-box*res,box*res):
				for zz in range(-box*res,box*res):
					tempscore = 0
					for w in range(0,len(graph)):
						if graph[w][0] != y:
							if graph[w][1] !=y:
								continue
						if graph[w][0] == y:
							tempscore = tempscore + abs(1 - (z/res - loc[graph[w][1]][0])**2 - (zz/res - loc[graph[w][1]][1])**2)
						else:
							tempscore = tempscore + abs(1 - (z/res - loc[graph[w][0]][0])**2 - (zz/res - loc[graph[w][0]][1])**2)
					if tempscore < score:
						score = tempscore
						bestx = z/res
						besty = zz/res
			loc[y][0] = bestx
			loc[y][1] = besty

	return loc

print(unit(g,n))