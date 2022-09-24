from py2neo import Graph, NodeMatcher, Node, Relationship, RelationshipMatcher
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk import download
import pandas
import uuid

download("stopwords")

graph = Graph("bolt://localhost:7687", auth=("neo4j", "admin"))
snowballStemmer = SnowballStemmer("portuguese")


def lematize_words(word):
    word = word.replace(",", "")
    return " ".join(
        [
            snowballStemmer.stem(wrd).replace(".", "")
            for wrd in word.split()
            if wrd not in stopwords.words("portuguese")
        ]
    )


def verify_node_exists(dict_verification: dict):
    is_exist = NodeMatcher(graph).match("Spent", **dict_verification).exists()
    return is_exist


def get_nodo(nodo):
    div_lematizada = lematize_words(nodo)
    if verify_node_exists({"lemmatized": div_lematizada}):
        nodo = NodeMatcher(graph).match("Spent", lemmatized=div_lematizada).first()
        return nodo
    else:
        vlr_uuid = uuid.uuid4().hex
        is_raiz = (
            False if nodo not in ["Despesas Fixas", "Despesas Temporárias"] else True
        )
        tx = graph.begin()
        tx.create(
            Node(
                "Spent",
                div=nodo,
                lemmatized=div_lematizada,
                uuid=vlr_uuid,
                base=True,
                haveChildren=False,
                is_raiz=is_raiz,
            )
        )
        graph.commit(tx)
        nodo = NodeMatcher(graph).match("Spent", uuid=vlr_uuid).first()
        return nodo


def create_relationship(nodo_pai, nodo_filho, relationship_name):
    rl_match = RelationshipMatcher(graph).match(
        (nodo_pai, nodo_filho), relationship_name
    )
    if len(rl_match.all()) == 0:
        tx = graph.begin()
        data = {
            "from": nodo_pai["uuid"],
            "to": nodo_filho["uuid"],
            "div_from": nodo_pai["from"],
            "div_to": nodo_filho["to"],
        }
        relation = Relationship(nodo_pai, relationship_name, nodo_filho, **data)
        tx.create(relation)
        graph.commit(tx)


def create_nodos_despesas():
    df = pandas.read_csv("./data/despesas.csv")
    for text_pai, text_filho in df.values:
        nodo_pai = get_nodo(text_pai)
        nodo_pai["haveChildren"] = True
        graph.push(nodo_pai)
        nodo_filho = get_nodo(text_filho)
        create_relationship(nodo_pai, nodo_filho, "SUB_TIPO")


if __name__ == "__main__":
    create_nodos_despesas()
