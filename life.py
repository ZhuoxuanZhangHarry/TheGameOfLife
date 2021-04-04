import picture


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False
        self.last = False

    def countNeighbors(self, cells):
        count = 0

        # get the width and height of the canvas
        width = len(cells)
        height = len(cells[0])

        # use the donut
        north_y = (self.y - 1) % height
        east_x = (self.x + 1) % width
        south_y = (self.y + 1) % height
        west_x = (self.x - 1) % width

        north_neighbor = cells[self.x][north_y]
        northeast_neighbor = cells[east_x][north_y]
        east_neighbor = cells[east_x][self.y]
        southeast_neighbor = cells[east_x][south_y]
        south_neighbor = cells[self.x][south_y]
        southwest_neighbor = cells[west_x][south_y]
        west_neighbor = cells[west_x][self.y]
        northwest_neighbor = cells[west_x][north_y]

        if north_neighbor.last:
            count += 1
        if northeast_neighbor.last:
            count += 1
        if east_neighbor.last:
            count += 1
        if southeast_neighbor.last:
            count += 1
        if south_neighbor.last:
            count += 1
        if southwest_neighbor.last:
            count += 1
        if west_neighbor.last:
            count += 1
        if northwest_neighbor.last:
            count += 1

        return count

    def update(self, cells):
        count = self.countNeighbors(cells)
        if count >= 4:
            self.alive = False
        if count <= 1:
            self.alive = False
        if count == 2:
            self.alive = self.alive
        if count == 3:
            self.alive = True


class Board:
    def __init__(self, width, height):
        self.cells = []
        for x in range(width):
            self.cells.append([])
            for y in range(height):
                self.cells[x].append(Cell(x, y))

    def initialize(self, setup):
        width = len(self.cells)
        height = len(self.cells[0])
        if setup == 1:
            self.cells[width // 2][height // 2].alive = True
            self.cells[width // 2][height // 2 - 1].alive = True
            self.cells[width // 2 + 1][height // 2].alive = True
            self.cells[width // 2 - 1][height // 2].alive = True
            self.cells[width // 2 - 1][height // 2 + 1].alive = True

    def update(self):
        width = len(self.cells)
        height = len(self.cells[0])
        for x in range(width):
            for y in range(height):
                self.cells[x][y].last = self.cells[x][y].alive
        for x in range(width):
            for y in range(height):
                self.cells[x][y].update(self.cells)

    def helper(self, canvas, width, height):
        for x in range(width):
            for y in range(height):
                if self.cells[x][y].alive:
                    canvas.setFillColor(255, 0, 0)
                    canvas.drawRectFill(x * 10, y * 10, 10, 10)
                else:
                    canvas.setFillColor(255, 255, 255)
                    canvas.drawRectFill(x * 10, y * 10, 10, 10)

    def draw(self, canvas, force):
        width = len(self.cells)
        height = len(self.cells[0])
        if force:
            self.helper(canvas, width, height)
            return
        for x in range(width):
            for y in range(height):
                if self.cells[x][y].alive != self.cells[x][y].last:
                    if self.cells[x][y].alive:
                        canvas.setFillColor(255, 0, 0)
                        canvas.drawRectFill(x * 10, y * 10, 10, 10)
                    else:
                        canvas.setFillColor(255, 255, 255)
                        canvas.drawRectFill(x * 10, y * 10, 10, 10)


def main():
    setup = int(input("Hey you! Enter a integer!!!!(1, otherwise is not implemented)"))
    display = Board(50, 80)
    Board.initialize(display, setup)
    canvas = picture.Picture(500, 800)
    Board.draw(display, canvas, True)
    for i in range(100):
        Board.update(display)
        Board.draw(display, canvas, False)
    input()


if __name__ == '__main__':
    main()
