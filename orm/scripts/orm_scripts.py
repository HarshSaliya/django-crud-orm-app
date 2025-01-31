
from orm.models import Restaurant , Rating ,Sale ,Blog , Author , Entry
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from django.db.models import Avg , F , Max

    

def run():
    a = Entry.objects.aggregate(Max("rating"))  
    print(a) 


# find avg 

    # a = Entry.objects.aggregate(Avg("rating"))  
    # print(a) 

# find id form list
#  a=Blog.objects.filter(pk__in=[1,3])
#     print(a)


# compare 
    # a=Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks"))

    # print(a)

#Find similar word or uppercase or lowecase handle
    # a=Entry.objects.get(headline__iexact='Ek tha coder')
    # print(a)


    #  a=Entry.objects.get(headline__contains='Ek')  #if any one word find its show output
    # print(a)

#Find Excet same match value
    # a=Entry.objects.get(headline__exact='Ek Tha Coder')
    # print(a)

    #  a=Entry.objects.get(headline='Ek Tha coder')
    # print(a)


# find less than values
    # a=Entry.objects.filter(pub_date__lte='2025-01-01')
    # print(a)

# order by 
# a=Entry.objects.order_by('headline')
    # print(a)

# return specifuc data using slince
    # a=Author.objects.all()[:3]
    # print(a)
    

# Find By first name in sql like operator

    # a=Entry.objects.filter(headline__startswith='Ek ')
    # print(a)

#update data using id

    # b=Blog.objects.get(id =1)
    # b.name="Harsh"
    # b.save()
  
  

#delete data using id


#   rest=Restaurant.objects.get(id =2)
   
#     rest.delete()
#     print(rest)
  


# Find data of child table  using main table  ( Foreignkey )
    # rest=Restaurant.objects.first()
    # print(rest.rating_set.all())
    # rest.save()


# update data 

    # rest=Restaurant.objects.first()
    # rest.name="PapaRazi"
    # rest.save()



#Find data by coulm name 
 
    # print(Restaurant.objects.first().latitude)



#Foreinkey model insert data

# def run():
 
#     rest =Restaurant.objects.first()
#     user=User.objects.first()

#     Rating.objects.create(user=user,restaurant=rest ,rating=5 )

#     print(connection.queries)



#add new data
# def run():

#     resaurant = Restaurant()
#     resaurant.name = "Pizza Hut"
#     resaurant.date_opened=timezone.now()
#     resaurant.latitude=50.2
#     resaurant.longitude=50.2
#     resaurant.restaurant_choice=Restaurant.TypeChoice.Indian
#     print("this wil run")
#     resaurant.save()

#run() its the entry point 



#find first record

  # show=Restaurant.objects.first()
    # print(show)


# Insert New data in database like sql



# def run():
 
#     Restaurant.objects.create(
#         name="PizzA",
#         date_opened=timezone.now(),
#         latitude=50.2,
#         longitude=51.2,
#         restaurant_choice=Restaurant.TypeChoice.Chinese

#     )
 

#     print(connection.queries)



#Count total row

#  cnt=Restaurant.objects.count()
#     print(cnt)
