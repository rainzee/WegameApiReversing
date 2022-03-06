# By：@rainzee
# At：2022.3.6

import json
import requests

#封装API主体函数
def check():

	#API常量
	QUERY_BY_NICK = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_lol_proxy/query_by_nick'
	GET_BATTLE_TOPBAR_INFO = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_lol_proxy/get_battle_topbar_info'
	BATTLE_LIST = 'https://m.wegame.com.cn/api/trpc/Proxy/Forward/trpc.wegameapp.lol_common_service.DataLogic/GetBattleList'
	header = {
	    'User-Agent': 'WeGame/1778 CFNetwork/1121.2.2 Darwin/19.3.0',
	    'Host': 'm.wegame.com.cn',
	    'Content-Type': 'application/json'
	}

	cookie = {
	    'tgp_id': '171450862',
	    'tgp_ticket': '482C776A7C46D4ED227F60694B209BECA840474E86AB5C0F30570F485ADFB7AA98420C425BBFF3D3AE8E9E93A27878F9C3C83D77181C880D00270A92CAE96B212BCE5A9B7887E04DA44355C18B394CF89CBB3DFC8169279D8EC08E75D3768B80837C5A5D0397F336EEC2A9E48159556B9EDF698414B061F323E94F9E9CC526BA'
	}

	data = '{"search_nick": "longbitcoin"}'
	response = requests.post(url=QUERY_BY_NICK, headers=header, cookies=cookie, data=data, timeout=8)
	json_return = json.loads(response.text)
	json_object = json.loads(response.text)
	json_formatted_str = json.dumps(json_object, indent=4, sort_keys=True)
	print(json_formatted_str)
	slol_id = json_return["data"]["player_list"][0]["slol_id"]
	done_data = {
	    "area_id": 3,
	    "area_name": "",
	    "filter_type": 0,
	    "game_id": 26,
	    "limit": 10,
	    "offset": 0,
	    "slol_id": slol_id,
	    "totalNum": 0
	}
	data = json.dumps(done_data)
	response = requests.post(url=GET_BATTLE_TOPBAR_INFO, headers=header, cookies=cookie, data=data, timeout=8)
	json_object = json.loads(response.text)
	json_formatted_str = json.dumps(json_object, indent=4, sort_keys=True)
	print(json_formatted_str)
	response = requests.post(url=BATTLE_LIST, headers=header, cookies=cookie, data=data, timeout=8)
	json_object = json.loads(response.text)
	json_formatted_str = json.dumps(json_object, indent=4, sort_keys=True)
	print(json_formatted_str)


check()
