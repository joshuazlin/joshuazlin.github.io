from copy import deepcopy


def pick(x):
	#input an integer x, and returns all x-long arrays of 0s and 1s
	xx = [0] * x
	xxxx = []
	for xxx in range(0,2**x):
		xxxx.append(deepcopy(xx))
		for yyy in range(x-1, -1, -1):
			if xx[yyy] == 0:
				for yyyy in range(x-1, yyy, -1):
					xx[yyyy] = 0
				xx[yyy] = 1
				break
	return(deepcopy(xxxx))

def powerSet(x):
	#insert a set x, output the set P(x)
	y = [0] * len(x)
	xxx = []
	for yy in range(0,2**len(x)):
		xxxx = []
		for xx in range(0,len(x)):
			if (y[xx] == 1):
				xxxx.append(deepcopy(x[xx]))
		for yyy in range(len(x)-1, -1, -1):
			if y[yyy] == 0:
				for yyyy in range(len(x)-1, yyy, -1):
					y[yyyy] = 0
				y[yyy] = 1
				break
		xxx.append(deepcopy(xxxx))
	return(deepcopy(xxx))

def union(x,y):
	#returns the union of the sets x and y
	xx = []
	for xxx in range(0,len(x)):
		if x[xxx] not in xx:
			xx.append(x[xxx])
	for xxx in range(0,len(y)):
		if y[xxx] not in xx:
			xx.append(y[xxx])
	return(deepcopy(xx))

def intersection(x,y):
	#returns the intersection of the sets x and y
	xx = []
	for xxx in range(0,len(x)):
		for xxxx in range(0,len(y)):
			if x[xxx] == y[xxxx]:
				xx.append(x[xxx])
				break
	return(deepcopy(xx))


def subset(x,y):
	#returns whether or not x (a set of numbers) is an element of y (a set of sets of numbers)
	for xx in range(0,len(y)):
		xy = 1
		for xxx in range(0,len(x)):
			if (x[xxx] not in y[xx]):
				xy = 0
				break
		if xy == 1:
			return 1
	return 0

def legal(x):
	#is the set x of sets a legal topology??
	xxx = 0
	for xx in range(0,len(x)):
		if len(x[xx]) == 0:
			xxx = 1
			break
	if xxx == 0:
		return 0
	xxx = 0
	for xx in range(0,len(x)):
		if len(x[xx]) == n:
			xxx = 1
			break
	if xxx == 0:
		return 0
	xx = pick(len(x))
	for xxx in range(0,len(xx)):
		y = []
		yy = -1
		for xxxx in range(0,len(x)):
			if (xx[xxx][xxxx] == 1):
				if yy == -1:
					yy = deepcopy(x[xxxx])
				y = union(y,deepcopy(x[xxxx]))
				yy = intersection(yy,deepcopy(x[xxxx]))
		if subset(deepcopy(y),deepcopy(x)) == 0:
			return 0
		if yy != -1:
			if subset(deepcopy(yy),deepcopy(x)) == 0:
				return 0
	return 1

def permute(x):
	#return a set containing all the permutations of the elements in the *SET* x
	if len(x) == 1:
		return([deepcopy(x)])
	if len(x) == 2:
		return(deepcopy([[x[0],x[1]],[x[1],x[0]]]))
	y = []
	for yy in range(0,len(x)):
		xx = permute(deepcopy(x[0:yy] + x[yy+1:]))
		for xxx in range(0,len(xx)):
			y.append(deepcopy([x[yy]] + xx[xxx]))
	return(deepcopy(y)) 


def isomorphic(x,y,xx):
	#checks whether two topologies, x and y, defined on xx points, are isomorphic
	if (len(x) != len(y)):
		return 0
	xy = permute(list(range(xx)))
	for yy in range(0,len(xy)):
		xxx = deepcopy(x)
		for yyy in range(0,len(xxx)):
			for yyyy in range(0,len(xxx[yyy])):
				xxx[yyy][yyyy] = xy[yy][xxx[yyy][yyyy]]
		xyxyxyxy = 0
		for yyy in range(0,len(xxx)):
			xyxy = 0
			for yyyy in range(0,len(y)):
				if len(intersection(deepcopy(xxx[yyy]),deepcopy(y[yyyy]))) == len(xxx[yyy]):
					if len(union(deepcopy(xxx[yyy]),deepcopy(y[yyyy]))) == len(xxx[yyy]):
						xyxy = 1
						xyxyxyxy = xyxyxyxy + 1
						break
		if xyxyxyxy == len(xxx):
			return 1
	return 0



def close(x):
	#given a bad-topology x (with empty and full in it though), take all finite intersections,
	#then arbitrary unions to find the smallest topology that 'covers' x
	xx = pick(len(x))
	y = []
	for yy in range(0,len(xx)):
		xxyy = 0
		for xy in range(0,len(x)):
			if xx[yy][xy] == 1:
				yyy = deepcopy(x[xy])
				xxyy = 1
				break
		if xxyy == 0:
			continue
		for xy in range(0,len(x)):
			if xx[yy][xy] == 1:
				yyy = intersection(deepcopy(yyy),deepcopy(x[xy]))
		y.append(deepcopy(yyy))
	y = pickle(deepcopy(y))
	xyyx = []
	xx = pick(len(y))
	for yy in range(0,len(xx)):
		yyy = []
		for xy in range(0,len(y)):
			if xx[yy][xy] == 1:
				yyy = union(deepcopy(yyy),deepcopy(y[xy]))
		xyyx.append(deepcopy(yyy))
	xyyx = deepcopy(pickle(deepcopy(xyyx)))
	return(deepcopy(xyyx))


def equalSet(x,y):
	#this finds out if two sets of numbers, x and y, are equal
	if len(intersection(deepcopy(x),deepcopy(y))) == len(union(deepcopy(x),deepcopy(y))):
		return 1
	return 0


def pickle(x):
	#this removes any redundant open sets in topology x
	#WARNING: THis is dumb way. Im tired. Get on with it.
	y = []
	for xx in range(0,len(x)):
		xy = 0
		for xxx in range(xx+1,len(x)):
			if equalSet(deepcopy(x[xx]),deepcopy(x[xxx])) == 1:
				xy = 1
				break
		if xy == 0:
			y.append(deepcopy(x[xx]))
	return(deepcopy(y))



#Define functions in terms of x and y cos yea
#pick(x) - input integer x, return set of all x-long arrays made of 0s and 1s
#powerSet(x) - insert a set x, output the powerset P(x). Seems like it works for everything
#union(x,y) - union of the sets of numbers x and y
#intersection(x,y) - intersection of the sets of numbers x and y
#subset(x,y) - returns whether or not x (a set of numbers) is an element of y (a set of sets of numbers)
#legal(x) - returns whether or not x is a legal topology
#permute(x) - returns the set of permutations of the set x (maybe only for x = set of numbers, list(range))
#isomorphic(x,y,xx) - returns whether or not the two topologies x,y defined on xx points are isomorphic
#close(x) - returns the smallest topology that includes the given set x
#equalSet(x,y) - returns whether or not two sets of numbers x,y are equal
#pickle(x) - removes any redundant sets from a topology x



n = 3
#n is the number of vertices
s = powerSet(list(range(0,n)))
#s is going to be the power-set of n vertices
t = []
#t is going to be the set of all topologies on n vertices (ignoring isomorphic ones)
b = powerSet(s)
#b is going to be the power-set of s; i.e. all topologies (even the ill-defined ones)
g = []
#g is going to be the set of all topologies on n vertices (up to isomorphism!!)


v = [[[],list(range(0,n))]]
#v is the set of vertices (which are the toplogies)
e = []
#e is the set of directed edges. What can become what in one move.
u = [0]
#u is the set of unexplored nodes so far. 


while len(u) > 0:
	#now we are looking at the u[0]-th vertex (in the v array)
	a = pick(n)
	for b in range(0,len(a)):
		#now we are thinking about adding a open set defined by a[b] (which elements are 1) into the mix
		d = []
		for f in range(0,len(a[b])):
			if a[b][f] == 1:
				d = d + [f]
		c = deepcopy(close(pickle(deepcopy(v[u[0]]) + [deepcopy(d)])))
		if len(c) == len(v[u[0]]):
			continue
		if legal(c) == 0:
			continue
		h = 0
		for f in range(0,len(v)):
			if (isomorphic(deepcopy(v[f]),deepcopy(c),n) == 1):
				h = 1
				e.append([u[0],f])
				break
		if h == 0:
			v.append(deepcopy(c))
			e.append([u[0],len(v)-1])
			u.append(len(v)-1)
	del u[0]


print(pickle(e))


