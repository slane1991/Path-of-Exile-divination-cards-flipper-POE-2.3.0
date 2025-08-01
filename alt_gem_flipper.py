import requests

def get_lab_alt_gem_flips(league_name: str):
    """
    Finds profitable alternate quality gem flipping opportunities in the given PoE league.

    Args:
        league_name (str): The name of the Path of Exile league.

    Returns:
        List[dict]: List of flipping opportunities, each as a dict with keys:
            - base
            - alt
            - gem_level
            - gem_quality
            - base_value
            - alt_value
            - profit
            - margin
    """
    url = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=SkillGem"
    response = requests.get(url)
    data = response.json()["lines"]

    base_gems = {}
    alt_gems = {}

    for gem in data:
        name = gem["baseType"]
        if "Trarthus" in name:
            continue  # Skip Trarthus gems

        level = gem.get("gemLevel")
        quality = gem.get("gemQuality")
        key = (name, level, quality)

        if " of " in name:
            # Treat as alternate gem
            base_name = name.split(" of ")[0]
            alt_gems.setdefault((base_name, level, quality), []).append(gem)
        else:
            # Treat as base gem
            base_gems[key] = gem

    opportunities = []

    for key, base_gem in base_gems.items():
        base_name, level, quality = key
        base_value = base_gem.get("divineValue", 0)

        if key in alt_gems:
            for alt_gem in alt_gems[key]:
                alt_value = alt_gem.get("divineValue", 0)
                profit = alt_value - base_value
                if profit > 0:
                    margin = (profit / base_value) * 100 if base_value > 0 else 0
                    opportunities.append({
                        "base": base_name,
                        "alt": alt_gem["baseType"],
                        "gem_level": level,
                        "gem_quality": quality,
                        "base_value": base_value,
                        "alt_value": alt_value,
                        "profit": profit,
                        "margin": margin
                    })

    # Sort by profit descending
    opportunities.sort(key=lambda x: x["profit"], reverse=True)
    return opportunities