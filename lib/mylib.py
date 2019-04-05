import csv

def read_csv(f_nm):
	data = []
	with open(f_nm, 'r') as csv_f:
		csv_r = csv.reader(csv_f, delimiter=',')
		for row in csv_r:
			data.append(row)
	csv_f.close()
	return data

def str2arr(A):
	A = A.split(',')
	A = [int(i) for i in A]
	return A

def comp_col(c0, c1):
	return c0[0] == c1[0] and c0[1] == c1[1] and c0[2] == c1[2]
    
class Queue:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def enQueue(self, data):
		self.items.append(data)
	def deQueue(self):
		return self.items.pop(0)

def flood_fill (img, p, c):
	c.append(255)
	Q = Queue()
	Q.enQueue(p)
	while (not Q.is_empty()):
		p = Q.deQueue()
		if img[p[0]][p[1]][3] == 0:
			img[p[0]][p[1]] = c
			Q.enQueue([p[0] - 1, p[1] - 1])
			Q.enQueue([p[0] - 1, p[1]])
			Q.enQueue([p[0] - 1, p[1] + 1])
			Q.enQueue([p[0], p[1] - 1])
			Q.enQueue([p[0], p[1] + 1])
			Q.enQueue([p[0] + 1, p[1] - 1])
			Q.enQueue([p[0] + 1, p[1]])
			Q.enQueue([p[0] + 1, p[1] + 1])
	return img