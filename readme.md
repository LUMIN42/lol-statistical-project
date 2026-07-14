# Statistical Project

## Dataset

My last ~120 League of Legends matches which I extracted as a task in the data engineering subject.

## Important Disclaimer

I have decided to include db credentials inside the project so that you can try fetching the data yourself.
It's a database shared by everyone in the data engineering course and if the credentials leaked, I could be in some
trouble.
Therefore, please do not share the repository without my approval.

## Project Structure

Each Hypothesis I am testing has its own repository folder.

Each folder contains 3 files:

- (folder_name).ipynb are Jupyter notebooks commenting on the relevant results.
  This is what you mainly should be checking. It loads data from data.csv.
- Data.csv is the fetched data. It is usually very bare-bones, since the logic is done in the create_data scripts.
- Create_data fetches the relevant data from the SQL db. It imports the db connection from db.py.
  You do not need to run this, since the data is already pre-downloaded in the repository.

## Analyses

- [AP AD split win-rate analysis](ap_ad_split/ap_ad_split.ipynb)
- [Dragon soul win-rate analysis](dragon_soul_winrate/dragon_soul.ipynb)
- [with vs without my friend win-rate comparison](friend_wr/friend.ipynb)
