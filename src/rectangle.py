from points import get_quadrant, get_x, get_y, make_decart_point


# BEGIN (write your solution here)
def make_rectangle(point, width, height):
    right_top_point = make_decart_point(get_x(point) + width, get_y(point))
    right_bottom_point = make_decart_point(get_x(right_top_point), get_y(right_top_point) - height)
    left_bottom_point = make_decart_point(get_x(point), get_y(point) - height)
    
    rectangle = {
        'left_top_point': point, 
        'right_top_point': right_top_point, 
        'left_bottom_point': left_bottom_point, 
        'right_bottom_point': right_bottom_point
        }
    return rectangle


def get_start_point(rectangle):
    return rectangle['left_top_point']


def get_width(rectangle):
    x1 = get_x(rectangle['left_top_point'])
    x2 = get_x(rectangle['right_top_point'])

    return x2 - x1


def get_height(rectangle):
    y1 = get_y(rectangle['left_top_point'])
    y2 = get_y(rectangle['left_bottom_point'])

    return y2 - y1


def contains_origin(rectangle):
    print(f'{rectangle=}')
    left_top_point_quadrant = get_quadrant(get_start_point(rectangle))
    right_top_point_quadrant = get_quadrant(rectangle['right_top_point'])
    left_bottom_point_quadrant = get_quadrant(rectangle['left_bottom_point'])
    right_bottom_point_quadrant = get_quadrant(rectangle['right_bottom_point'])
    print(f'{left_top_point_quadrant=}')
    print(f'{right_top_point_quadrant=}')
    print(f'{left_bottom_point_quadrant=}')
    print(f'{right_bottom_point_quadrant=}')
    return left_top_point_quadrant != left_bottom_point_quadrant and left_bottom_point_quadrant is not None
# END

p = make_decart_point(-4, 3)

print(contains_origin(make_rectangle(p, 4, 3)))

# print(get_quadrant(p))