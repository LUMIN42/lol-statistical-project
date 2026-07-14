# Statistical Project

## Dataset

My last ~120 League of Legends matches which I extracted as a task in the data engineering subject.

## Project Structure

Each Hypothesis I am testing has its own repository folder.

Each folder contains 3 files:

- (folder_name).ipynb are Jupyter notebooks commenting on the relevant results.
  This is what you mainly should be checking. It loads data from data.csv.
- Data.csv is the fetched data. It is usually very bare-bones, since the logic is done in the create_data scripts.
- Create_data fetches the relevant data from the SQL db. It imports the db connection from db.py.
  However, since this repository does not contain db password in order to be easier to share, they do not work. 

## Analyses

- [AP AD split win-rate analysis](ap_ad_split/ap_ad_split.ipynb)
- [Dragon soul win-rate analysis](dragon_soul_winrate/dragon_soul.ipynb)
- [with vs without my friend win-rate comparison](friend_wr/friend.ipynb)
