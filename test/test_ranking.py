from ranking.ranking import Ranking


rank=Ranking("ranking/documents.json","ranking/index.json")

def test_read_query():
    resu=["wikipédia","lacombe"]
    rank.read_query("Wikipédia Lacombe")
    assert resu == rank.query_tokens 