from app.modules.core.graph_models import User as UserNode, Spent


class SpentNodeRepository:
    async def relating_node(self, user_node: UserNode):
        spending_base = Spent().nodes.filter(base=True)
        for spent_node in spending_base:
            spent_node.user.connect(user_node)

    async def filter_source_spending(self, user_node: UserNode):
        return user_node.spending.filter(is_raiz=True).all()

    async def filter_sub_spending(self, user_node: UserNode, spent_uuid: str):
        spent = user_node.spending.filter(uuid=spent_uuid).get()
        return spent, spent.spending
