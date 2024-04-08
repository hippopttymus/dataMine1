#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
import networkx as nx

#G = nx.read_adjlist('graph.csv', delimiter=',')

D = nx.DiGraph()
with open('graph.csv','r') as f:
    for line in f:
        line=line.split(',')#split the line up into a list - the first entry will be the node, the others his friends
        if len(line)==1:#in case the node has no friends, we should still add him to the network
            if line[0].strip() not in D:
                nx.add_node(line[0].strip())
        else:#in case the node has friends, loop over all the entries in the list
            focal_node = line[0]#pick your node
            for friend in line[1:]:#loop over the friends
                D.add_edge(focal_node.strip(),friend.strip())#add each edge to the graph

nx.draw(D, with_labels=True )
#print(D.nodes(),G.edges())
#print(G.nodes(),G.edges())


# In[2]:


pr1 = nx.pagerank(D)

for x in pr1:
    print(x + " weight " + str(pr1[x]))
pos = nx.spiral_layout(D)
nx.draw(D, pos, nodelist=list(pr1.keys()), node_size=[round(v*3000) for v in pr1.values()] ,with_labels = True, node_color="#f86e00")
plt.show()


# In[4]:


import pandas as pd
from surprise import Dataset
from surprise import Reader

df = pd.read_csv('ratings_small_training.csv')

print(df)

reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(df[["userId", "movieId", "rating"]], reader)

testDf = pd.read_csv('ratings_small_test.csv')
testDf = testDf.reset_index()

print(testDf)


# In[5]:


from surprise import KNNWithMeans
sim_options = {
    "name": "cosine"
}
algo = KNNWithMeans(sim_options=sim_options)


# In[6]:


trainingSet = data.build_full_trainset()

algo.fit(trainingSet)


# In[7]:


predictions = []
for index, row in testDf.iterrows():
    prediction = algo.predict(row['userid'], row['movieid'])
    predictions.append(prediction.est)
    print(row['userid'], row['movieid'], round(prediction.est, 2))

testDf.insert(3, "rating", predictions, True)


# In[9]:


testDf.to_csv('ratings_small_test_Updated.csv', index = False) 


# In[ ]:




