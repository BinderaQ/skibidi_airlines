def create_mountains(width, height):
    mountain_range = []
    for row in range(height):
        mountain_row = ""
        for col in range(width):
            if row < height // 2:
                if col == 0 or col == width - 1:
                    mountain_row += "/"
                else:
                    mountain_row += " "
            else:
                if col == row - height // 2 or col == width - (row - height // 2) - 1:
                    mountain_row += "\ "
                else:
                    mountain_row += " "
        mountain_range.append(mountain_row)
    return mountain_range

def print_mountains(mountains):
    for row in mountains:
        print(row)


mountains = create_mountains(20, 10)
print_mountains(mountains) 