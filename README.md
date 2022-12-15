#Project Title
CodingTimeTask

#Project Description
The project is about creating a menu from 3 tables Topping, Food, FoodCategory 



#How to Install and Run the Project

First clone the code from the GitHub,

Then if you want to run it on Docker install it on your devise, 

Run this command "docker-compose up -d --build".

After that do this command for migration 

"docker-compose exec web python manage.py migrate". 

Then do this to create a super user 

"docker-compose exec web python manage.py createsuperuser". 

With the next step upload the data and open this url on the web 

"http://127.0.0.1:8000/api/v1/food/" to see the response of the backend


