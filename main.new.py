import numpy as np
import pandas as pd
import sys
import json

kuku = pd.read_csv('../python/database.csv')
kuku
print(kuku)



num_rating_df = kuku.groupby('Hostel_Name').count()['Hostel Rating Simple'].reset_index()
num_rating_df.rename(columns={'Hostel Rating Simple':'num_ratings'},inplace=True)
num_rating_df





avg_rating_df = kuku.groupby('Hostel_Name').mean()['Hostel Rating Simple'].reset_index()
avg_rating_df.rename(columns={'Hostel Rating Simple':'avg_rating'},inplace=True)
avg_rating_df





popular_df = kuku.merge(avg_rating_df,on='Hostel_Name')
yoyo=popular_df.merge(num_rating_df,on='Hostel_Name')






yoyo = yoyo[yoyo['num_ratings']>=2].sort_values('avg_rating',ascending=False).head(50)








yoyo['tags'] = yoyo['Hostel Rating'] + yoyo['Hostel Location'] + yoyo['Boys/Girls Hostel']




yoyo['tags'].apply(lambda x:[i.replace(" ","")for i in x])
yoyo





yoyo['tags'] = yoyo['tags'].apply(lambda x:x.lower())




yoyo





from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=500,stop_words='english')
    





vector = cv.fit_transform(yoyo['tags']).toarray()
vector





cv.get_feature_names()





from sklearn.metrics.pairwise import cosine_similarity




similarity = cosine_similarity(vector)




index = sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
 

def recommend(Hostel_Name):
    hostel_index = yoyo[yoyo['Hostel_Name'] == Hostel_Name].index[0]
    distances = similarity[hostel_index]
    n = set()
#     print(distances)
    hostel_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    for i in hostel_list:
        if( yoyo.iloc[i[0]].Hostel_Name != Hostel_Name):
            n.add(yoyo.iloc[i[0]].Hostel_Name)
    
    output = json.dumps(n, cls=SetEncoder)
    print(output)
recommend('scholar park')






