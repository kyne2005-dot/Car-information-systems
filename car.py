

class Car:
    def __init__(self,name,live,year, brand, color,type):
        if name not in["kyne","bron","caleb","jgod"]:
            raise ValueError("wrong name")
        if live not in["atlanta","gwinnett","johns creek","milton"]:
            raise ValueError("wrong place")
        if brand not in ["honda", "lexus", "tesla"]:
            raise ValueError("Wrong car")
        if color not in ["black", "white", "green"]:
            raise ValueError("Wrong color")
        if type not in["suv","coupe","truck","sedan"]:
            raise ValueError("wrong type")
        self.name=name
        self.live=live
        self.year=year
        self.brand = brand
        self.color = color
        self.type = type


def main():
    results = get_car()

    if results:
        print(f"Hi!\nMy name is {results.name} I live in {results.live} and drive a {results.year} {results.brand}, the color is {results.color} and it's a {results.type}.")
    else:
        print("You ran out of tries.")


def get_car():
    for i in range(3):
        try:
            name=input("What is ur name? ").lower()
            live=input("Where do u live? ").lower()
            year=(input("Enter year: "))
            if not year.isdigit() or int(year) <2000 or int(year)>2027:
                raise ValueError("Wrong year")
            brand = input("What car u drive? ").lower()
            color = input("What color is it? ").lower()
            type = input("What type is it? ").lower()

            return Car(name,live,year,brand, color,type)

        except (ValueError,AttributeError):
            print("Wrong information. Try again!")

    return None

main()

