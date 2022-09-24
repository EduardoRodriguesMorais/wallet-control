from app.modules.core.abstract_models import BaseModel
from tortoise import fields


class User(BaseModel):
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)

    def __str__(self):
        return {"class: ": self, "name: ": self.name, "email: ": self.email}.__str__()

    class Meta:
        table = "user"
        ordering = ["id", "-email"]
