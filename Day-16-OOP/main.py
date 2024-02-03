# from turtle import Turtle, Screen
import prettytable

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# timmy.color("black")
# timmy.left(90)
# timmy.forward(100)
# timmy.right(45)
# timmy.backward(141.4)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

print(table)