from ranking.ranking import Ranking



if __name__=="__main__":
    rank=Ranking("ranking/documents.json","ranking/index.json")
    rank.launh_ranking("sport")


