from ranking.ranking import Ranking


rank=Ranking("ranking/documents.json","ranking/index.json")

def test_read_query():
    resu=["wikipédia","lacombe"]
    rank.read_query("Wikipédia Lacombe")
    assert resu == rank.query_tokens 

def test_filtering():
    resu= [{'url': 'https://fr.wikipedia.org/wiki/Karine_Lacombe', 'id': 0, 'title': 'Karine Lacombe — Wikipédia'}]
    rank.filtering()
    assert resu == rank.filtered_documents