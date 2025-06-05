def match_outfits(body_type):
    suggestions = {
        "slim": ["High-waist jeans", "Slim-fit Kurti", "Crop Tops"],
        "curvy": ["A-line dresses", "Peplum tops", "Maxi skirts"],
        "athletic": ["Jumpsuits", "Wrap dresses", "Tapered trousers"]
    }
    return suggestions.get(body_type.lower(), ["Basic T-shirt", "Classic Jeans"])
