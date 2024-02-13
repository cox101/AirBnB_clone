import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id=str(uuid.uuid4())
        self.created_at=datetime.datetime.today() # Assigned when an instance is created
        self.updated_at=datetime.datetime.today() # Assigned when an instance is updated

    def __setattr__(self, self.updated_at, datetime.datetime.today()):
        super().__setattr__(self.updated_at, datetime.datetime.today())
        if name != 'updated_at':
            self.save()

    def __str__(self):
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"

    def save(self): # Updates the public instance attribute 'updated_at' with the current datetime
        self.updated_at = datetime.datetime.today()


    def to_dict(self):
        pass
