from riotwatcher import LolWatcher, ApiError
import pandas as pd

api_key = 'RGAPI-a3f07f7e-dfaf-4c4b-9af9-d572639914be'
watcher = LolWatcher(api_key)
reg = 'na1'
summoner_name = "Doublelift"

me = watcher.summoner.by_name(reg, summoner_name)
print(f"{summoner_name}'s summoner level is {me['summonerLevel']}")

rank = watcher.league.by_summoner(reg, me['id'])
print(f"a {rank[0]['tier'].lower()} {rank[0]['rank']} player with a winrate of {int(rank[0]['wins']) / (int(rank[0]['losses']) + int(rank[0]['wins']))}")


coi = {'riven': 92, 'camille': 164, 'kaisa': 145, 'yasuo': 157}

for name, id in coi.items():
    stats = watcher.champion_mastery.by_summoner_by_champion(reg, me['id'], id)
    print(f"{summoner_name} has mastery {stats['championLevel']} on {name} with {stats['championPoints']} points. ")