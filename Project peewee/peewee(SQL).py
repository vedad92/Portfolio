db=peewee.SqliteDatabase(':memory:')
database = db
db.connect()

def cheapest_dish(name, served_at, price_in_cents, ingredients) -> Model.Dish:
    
    with database:
        database.create_tables([name, served_at, price_in_cents, ingredients])
        cheapest_dish.create(name='bami', served_at='chinese', price_in_cents=2.50, ingredients='pasta')
        cheapest_dish.save()
    query=Dish.select().where(Dish.price_in_cents==2.50)
    for Dish in query:
        print(Dish.name, Dish.price_in_cents==2.50)

def vegetarian_dishes(name, is_vegetarian, is_vegan, is_glutenfree) -> List[models.Dish]:
   
    with database:
        database.create_tables([name, is_vegetarian, is_vegan, is_glutenfree])
        vegetarian_dishes.create(name='bami', is_vegetarian=True, is_vegan=True, is_glutenfree=True)
        vegetarian_dishes.save()
    query=Dish.select().where(Dish.is_vegetarian==True)
    for Dish in query:
        print(Dish.name, Dish.is_vegetarian==True)

def best_average_rating(name, open_since, opening_time, closing_time, restaurant, rating, comment) -> models.Restaurant and models.Rating:
   
    with database:
        database.create_tables([restaurant, rating, comment])
        best_average_rating.create(restaurant='Kanton', rating=10, comment='good')
        best_average_rating.save()
        database.create_tables([name, open_since, opening_time, closing_time])
        best_average_rating.create(name='Kanton', open_since=1990, opening_time=12.00, closing_time=24.00)
    query=(Restaurant
        .select(Restaurant, Rating)
        .join(Rating)
        .where(Restaurant.name=='Kanton'))
    for Restaurant in query:
        print(Restaurant.name, Restaurant.rating)

def add_rating_to_restaurant(restaurant, rating, comment) -> models.Rating:
   
    for Rating in Rating.select().where(Rating.restaurant == 'Kanton').update(Rating.restaurant=='Shenzhen'):
        print(Rating.restaurant)

def dinner_date_possible() -> List[models.Restaurant]:
   
    query=(Restaurant
        .select(Restaurant,Dish.is_vegan==True)
        .join(Dish)
        .where(Restaurant.opening_time<18.00, Restaurant.closing_time<24.00))
    for Restaurant in query:
        print(Restaurant.name, Dish.is_vegan==True, Restaurant.opening_time18.00, Restaurant.closing_time22.00)


def add_dish_to_menu(name, served_at, price_in_cents, ingredients) -> models.Dish:
   
    with database:
        database.create_tables([name, served_at, price_in_cents, ingredients])
        add_dish_to_menu.create(name='cheese pasta', served_at='dutch', price_in_cents=3.50, ingredients='cheese')
        add_dish_to_menu.save()
    query=Dish.select().where(Dish.ingredients == 'cheese')
    for Dish in query:
        print(Dish.name, Dish.ingredients=='cheese')
