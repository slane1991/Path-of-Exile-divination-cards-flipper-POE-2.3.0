import requests

def get_essence_flips(league_name: str):
    """
    Finds profitable essence flipping opportunities in the given PoE league.

    Args:
        league_name (str): The name of the Path of Exile league.

    Returns:
        List[dict]: List of flipping opportunities, each as a dict with keys:
            - essence_type
            - shrieking_value
            - deafening_value
            - profit
            - margin
    """
    url = f"https://poe.ninja/api/data/itemoverview?league={league_name}&type=Essence"
    response = requests.get(url)
    data = response.json()["lines"]

    # Collect essence prices by type and tier
    essence_prices = {}
    for essence in data:
        name = essence["name"]
        value = essence["chaosValue"]

        if " Essence of " not in name:
            continue  # Skip Remnants or special essences

        try:
            tier, essence_type = name.split(" Essence of ", 1)
        except ValueError:
            continue

        if essence_type not in essence_prices:
            essence_prices[essence_type] = {}

        essence_prices[essence_type][tier] = value

    # Analyze for flipping opportunities
    opportunities = []
    for etype, tiers in essence_prices.items():
        shrieking = tiers.get("Shrieking")
        deafening = tiers.get("Deafening")

        if shrieking and deafening:
            total_cost = 3 * shrieking
            profit = deafening - total_cost
            if profit > 0:
                margin = (profit / total_cost) * 100
                opportunities.append({
                    "essence_type": etype,
                    "shrieking_value": shrieking,
                    "deafening_value": deafening,
                    "profit": profit,
                    "margin": margin
                })

    # Sort by descending profit
    opportunities.sort(key=lambda x: x["profit"], reverse=True)
    return opportunities