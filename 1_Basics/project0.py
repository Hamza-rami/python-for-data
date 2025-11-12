class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def display_task(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Year: {self.year}")

    def change_director(self, new):
        self.director = new


movie1 = Movie("Inception", "Christopher Nolan", "2010")
movie2 = Movie("The Godfather", "Francis Coppola", "1972")
movie3 = Movie("Parasite", "Bong Joon-ho", "2016")

print("----- List of movies -----\n")
movie1.display_task()
print()
movie2.display_task()
print()
movie3.display_task()

movie1.change_director("dadas")
movie2.change_director("jackie chan")
movie3.change_director("the rock")

print("\n----- List of movies after modification -----\n")
movie1.display_task()
print()
movie2.display_task()
print()
movie3.display_task()
