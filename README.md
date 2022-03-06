# WegameApi逆向笔记

### 接口以及相关功能

- query_by_nick 通过ID查询大区所有角色
- get_battle_topbar_info 角色信息
- battle_list 对局列表
- battle_details 对局详情
- get_often_used 常用英雄

```python
battle_list = 'https://m.wegame.com.cn/api/trpc/Proxy/Forward/trpc.wegameapp.lol_common_service.DataLogic/GetBattleList'
battle_details = 'https://m.wegame.com.cn/api/trpc/Proxy/Forward/trpc.wegameapp.lol_common_service.DataLogic/GetBattleDetail'
query_by_nick = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_lol_proxy/query_by_nick'
get_battle_topbar_info = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_lol_proxy/get_battle_topbar_info'
get_often_used = 'https://m.wegame.com.cn/api/mobile/lua/proxy/index/mwg_lol_proxy/get_often_used_champion'
```

### 请求响应例子

#### query_by_nick请求例子

```python
{"search_nick": "longbitcoin"}
```

#### query_by_nick响应例子

```python
{
  "msg": "succ",
  "code": 0,
  "data": {
    "result": 0,
    "player_list": [
      {
        "tgp_id": "437685496",
        "gender": 0,
        "game_nick": "LongBitcoin",
        "area_id": 3,
        "slol_id": "Yrdrw0jzNQL",
        "icon_url": "http://down.qq.com/lolapp/lol/summoner/profileicon/5030.jpg",
        "rank_title": "铂金IV"
      }
    ]
  }
}
```

#### get_battle_topbar_info请求例子

```python
{
  "area_id": 3,
  "area_name": "",
  "filter_type": 0,
  "game_id": 26,
  "limit": 10,
  "offset": 0,
  "slol_id": "Yrdrw0jzNQL",
  "totalNum": 0
}
```

#### get_battle_topbar_info响应例子

```python
{
  "msg": "succ",
  "code": 0,
  "data": {
    "total_time": 0,
    "recent_kda": 760,
    "tier": 2,
    "area_name": "祖安",
    "measure_unit": 0,
    "rank": 3,
    "skin_num": 1,
    "slol_id": "Yrdrw0jzNQL",
    "champion_num": 39,
    "total_games": 1186,
    "game_logo_url": "https://wegame.gtimg.com/g.26-r.c2d3c/helper/lol/assis/images/resources/usericon/5030.png",
    "game_level": 111,
    "area_id": 3,
    "gender": 0,
    "recent_win_rate": 57,
    "power_value": 33466,
    "recent_total_games": 158,
    "league_point": 62,
    "total_kill": 7318,
    "game_id": 26,
    "result": 0,
    "total_assist": 6218,
    "role_name": "LongBitcoin",
    "win_rate": 58,
    "online_zone_id": 0,
    "praise_time": 0,
    "total_placed": 4179,
    "recent_total_kill": 1213,
    "game_age": 0,
    "online_status": 0,
    "all_champion_num": 159,
    "all_skin_num": 1330
  }
}
```

#### battle_list请求例子

```python
{
  "area_id": 3,
  "area_name": "",
  "filter_type": 0,
  "game_id": 26,
  "limit": 10,
  "offset": 0,
  "slol_id": "Yrdrw0jzNQL",
  "totalNum": 0
}
```

#### battle_list响应例子

```python
{
  "code": 0,
  "msg": "succ",
  "data": {
    "continue_win": 1,
    "continue_lose": 0,
    "player_battle_brief_list": [
      {
        "battle_id": "3211174308",
        "battle_time": 1646388180,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 166,
        "game_result": 1,
        "game_score": 735,
        "kill_num": 8,
        "death_num": 8,
        "assist_num": 13,
        "ext_tag_id": 0,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3211171970",
        "battle_time": 1646386412,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 166,
        "game_result": 2,
        "game_score": 648,
        "kill_num": 2,
        "death_num": 7,
        "assist_num": 0,
        "ext_tag_id": 0,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3211108234",
        "battle_time": 1646383761,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 166,
        "game_result": 1,
        "game_score": 1101,
        "kill_num": 16,
        "death_num": 8,
        "assist_num": 15,
        "battle_flags": [
          6
        ],
        "ext_tag_id": 0,
        "position": 3,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3211106140",
        "battle_time": 1646382288,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 166,
        "game_result": 1,
        "game_score": 461,
        "kill_num": 2,
        "death_num": 4,
        "assist_num": 4,
        "ext_tag_id": 9,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3211132029",
        "battle_time": 1646379565,
        "game_mode_id": 3,
        "game_mode_name": "灵活组排",
        "champion_id": 90,
        "game_result": 1,
        "game_score": 922,
        "kill_num": 5,
        "death_num": 6,
        "assist_num": 11,
        "ext_tag_id": 0,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3210926594",
        "battle_time": 1646323098,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 90,
        "game_result": 2,
        "game_score": 319,
        "kill_num": 0,
        "death_num": 10,
        "assist_num": 7,
        "ext_tag_id": 2,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3210932589",
        "battle_time": 1646320621,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 166,
        "game_result": 2,
        "game_score": 891,
        "kill_num": 9,
        "death_num": 6,
        "assist_num": 5,
        "battle_flags": [
          3
        ],
        "ext_tag_id": 10,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3210889326",
        "battle_time": 1646318989,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 90,
        "game_result": 1,
        "game_score": 976,
        "kill_num": 7,
        "death_num": 5,
        "assist_num": 12,
        "ext_tag_id": 9,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3210873838",
        "battle_time": 1646316784,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 166,
        "game_result": 1,
        "game_score": 799,
        "kill_num": 6,
        "death_num": 6,
        "assist_num": 6,
        "ext_tag_id": 0,
        "position": 0,
        "win_with_less_teammate": 0
      },
      {
        "battle_id": "3210839301",
        "battle_time": 1646315125,
        "game_mode_id": 4,
        "game_mode_name": "单双排位",
        "champion_id": 81,
        "game_result": 1,
        "game_score": 469,
        "kill_num": 0,
        "death_num": 4,
        "assist_num": 2,
        "ext_tag_id": 9,
        "position": 0,
        "win_with_less_teammate": 0
      }
    ],
    "is_finish": 0,
    "next_index": 10,
    "result": 0,
    "errmsg": ""
  }
}
```

