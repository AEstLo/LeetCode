import heapq


class Food:
    def __init__(self, name, food_type, rating):
        self.name = name
        self.food_type = food_type
        self.rating = rating

    def setRating(self, newRating):
        self.rating = newRating

    def __repr__(self):
        return f"Food(name={self.name}, type={self.food_type}, rating={self.rating})"

    def getName(self):
        return self.name

    def getType(self):
        return self.food_type

    def __lt__(self, item):
        if self.rating == item.rating:
            return self.name < item.name
        return self.rating > item.rating

    def __eq__(self, item):
        return self.rating == item.rating and self.name == item.name


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.cuisines = {}
        for i in range(len(foods)):
            food = Food(foods[i], cuisines[i], ratings[i])
            self.foods[foods[i]] = food
            if cuisines[i] not in self.cuisines:
                self.cuisines[cuisines[i]] = []
            heapq.heappush(self.cuisines[cuisines[i]], food)

    def changeRating(self, food: str, newRating: int) -> None:
        food = self.foods[food]
        food.setRating(newRating)
        heapq.heapify(self.cuisines[food.getType()])

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0].getName()

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
