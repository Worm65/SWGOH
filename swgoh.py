#!/usr/bin/env python
# coding: utf-8

# In[2]:


Acc = int(input("how many shards per day: "))
ref = int(input("how many refreshes per day: "))
star = int(input("how many stars do you have? "))
shard = int(input("how many shards do you have? "))
energy = int(input("how much energy is the node? "))
constant = 0.33
shards_day = Acc*5*ref*constant
energy_use = (ref*5)*star
if star == 7:
    print(error)
    end = int(y)
elif star == 6:
    shard = shard + 230
    rem = 330-shard
elif star == 5:
    shard = shard + 145
    rem = 330-shard
elif star == 4:
    shard = shard + 80
    rem = 330-shard
elif star == 3:
    shard = shard + 50
    rem = 330-shard
elif star == 2:
    shard = shard + 25
    rem = 330-shard
elif star == 1:
    shard = shard + 10
    rem = 330-shard
days = rem/shards_day
t_energy = energy_use*days
print("you need "+str(rem)+" more shards")
print("this will take " + str(days) + " days to finish")
print("and will cost " + str(t_energy) + " energy")


# In[ ]:




