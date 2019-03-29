def flood_fill (x, y, col):
	if img[y][x] == [0, 0, 0]:
		return
	img[y][x] = col
	flood_fill(x-1, y, col)
	flood_fill(x+1, y, col)
	flood_fill(x, y-1, col)
	flood_fill(x, y+1, col)