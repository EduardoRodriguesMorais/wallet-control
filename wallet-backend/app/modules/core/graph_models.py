from neomodel import (
    StructuredNode,
    StringProperty,
    RelationshipTo,
    RelationshipFrom,
    BooleanProperty,
)


class Spent(StructuredNode):
    uuid = StringProperty(unique_index=True)
    base = BooleanProperty(default=False)
    div = StringProperty()
    have_children = BooleanProperty(default=False)
    user = RelationshipFrom("User", "SPENT")
    spending = RelationshipTo("Spent", "SUB_TIPO")
    spent = RelationshipFrom("Spent", "SUB_TIPO")


class User(StructuredNode):
    uuid = StringProperty(unique_index=True)
    name = StringProperty()
    email = StringProperty()
    spending = RelationshipTo("Spent", "SPENT")
