import datetime
from mongoengine import *

class Rating(Document):
	ratings = StringField() #user can input 1, 2, 3, 4 or 5 
	rate_name = StringField() #user name who rated
	comments = StringField() #description
	
class Post(Document):
	image_url = StringField() #path to the saved image
	image = FileField() #image
	owner_name = StringField() #user who uploads image, usually this would be a user id but no worries for now
        image_desc = StringField() #desciption of the photo
	avg_rate = FloatField() #takes the average of all the rating 
	rate = ListField(ReferenceField(Rating)) #or you can do ListField(ObjectIdField(required=True))
	
	
