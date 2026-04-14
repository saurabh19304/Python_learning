def http_error(status):
  match status:
    case 400:
      return "bad request"
    case 404:
      return "not found"
    case _:
      return "something went wrong"
    
    
# You can combine several literals in a single pattern using | (“or”):
# Copy
# case 401 | 403 | 404:
#     return "Not allowed"

class Point:
    __match_args__ = ('x', 'y')  #match_arument x and y as x= , y=
    def __init__(self, x, y):  #it is the constructor it sets data so that we do not have to do it manually
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


#for matching the named constants
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")        