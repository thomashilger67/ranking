import json 
import math 

class Ranking:
    def __init__(self,link_doc,link_index) -> None:
        self.documents=json.load(open(link_doc))
        self.index=json.load(open(link_index))
        
    def read_query(self,query):
        self.query=query
        self.query_lower=query.lower()
        self.query_tokens=self.query_lower.split()


    def filtering(self):
        try : 
            list_documents=self.documents
            resu=[]
            for token in self.query_tokens:
                
                if token in self.index.keys():
                    id_document=self.index[token].keys()
                    
                    new_doc=[]
                    for doc in list_documents:
                        if str(doc['id']) in id_document:
                            new_doc.append(doc)

                list_documents = [x for x in list_documents if x in new_doc]
            self.filtered_documents=list_documents
        except:
            self.filtered_documents=[]
            print("No document associated to this query! Try another query:")



    def ranking(self):
        freq={}
        for document in self.filtered_documents:
            
            count_title=len(document['title'].split())
            sum=0
            for token in self.query_tokens:

                
                count_query=[x==token for x in document['title'].lower().split()].count(True)
                
                freq_token=count_query/count_title
                sum=sum + math.log10(len(self.index)/len(self.filtered_documents))*(freq_token*(1.2+1))/(freq_token+1.2*(1-0.75+0.75*len(self.query_tokens)/count_title))
            
            freq[document['id']]=sum
        
        resu=dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
        self.ranked_score=resu
        ranked_documents={}
        ranked_documents['rank']=[]
        for key in resu.keys():
            final_document={}
            final_document['title']=self.documents[key]['title']
            final_document['url']=self.documents[key]['url']
            ranked_documents['rank'].append(final_document)

        ranked_documents['statistics']={"index":len(self.index),"filtered":len(self.filtered_documents)}
        self.ranked_documents=ranked_documents


    def launh_ranking(self,query):
        self.read_query(query)
        self.filtering()
        self.ranking()
        
        with open("results.json","w", encoding="utf8") as fp:
            json.dump(self.ranked_documents,fp,ensure_ascii=False)

            


