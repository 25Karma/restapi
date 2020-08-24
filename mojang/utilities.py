import requests

def get_player(player):
	r = requests.get('https://api.ashcon.app/mojang/v2/user/{player}'.format(player=player))
	json = dict(r.json())

	if r.status_code == 200:
		return {
			'success' : True,
			'username': json.get('username'),
			'uuid'    : json.get('uuid'),
			}

	if r.status_code == 400:
		return {
			'success' : False,
			'reason' : 'MOJANG_CALL_FAILED',
			'player' : player,
			}

	if r.status_code == 404:
		return {
			'success' : False,
			'reason' : 'MOJANG_PLAYER_DNE',
			'player' : player,
			}
		
	return {
		'success' : False,
		'reason' : 'UNKNOWN',
		'player' : player,
	}