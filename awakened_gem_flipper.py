import requests

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["lines"]

def get_beast_cost(league_name: str):
    beast_data = fetch_data(f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Beast")
    for beast in beast_data:
        if beast["name"] == "Wild Brambleback":
            return beast["divineValue"]
    raise ValueError("Wild Brambleback not found in beast data")

def get_awakened_gem_flips(league_name: str):
    """
    Finds profitable Awakened Gem flipping opportunities in the given PoE league.

    Args:
        league_name (str): The name of the Path of Exile league.

    Returns:
        List[dict]: List of flipping opportunities, each as a dict with keys:
            - gem
            - level1_value
            - level5_value
            - beast_cost
            - profit
            - margin
    """
    gems = fetch_data(f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=SkillGem")
    brambleback_cost = get_beast_cost(league_name)

    gem_dict = {}
    for gem in gems:
        name = gem["name"]
        gem_level = gem.get("gemLevel")
        divine_value = gem.get("divineValue")
        corrupted = gem.get("corrupted")

        if not name.startswith("Awakened") or corrupted:
            continue

        if name not in gem_dict:
            gem_dict[name] = {}

        # Only keep non-corrupted, level 1 and 5 gems
        if gem_level in [1, 5]:
            gem_dict[name][gem_level] = divine_value

    opportunities = []
    for name, levels in gem_dict.items():
        lvl1 = levels.get(1)
        lvl5 = levels.get(5)

        if lvl1 and lvl5:
            beast_cost = 4 * brambleback_cost
            profit = lvl5 - lvl1 - beast_cost
            margin = (profit / (lvl1 + beast_cost)) * 100 if (lvl1 + beast_cost) > 0 else 0

            if profit > 0:
                opportunities.append({
                    "gem": name,
                    "level1_value": lvl1,
                    "level5_value": lvl5,
                    "beast_cost": beast_cost,
                    "profit": profit,
                    "margin": margin
                })

    return sorted(opportunities, key=lambda x: x["profit"], reverse=True)