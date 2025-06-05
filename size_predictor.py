def estimate_size(height_cm, weight_kg):
    if height_cm < 160 and weight_kg < 50:
        return "S"
    elif 160 <= height_cm <= 175 and 50 <= weight_kg <= 70:
        return "M"
    elif height_cm > 175 and weight_kg > 70:
        return "L"
    else:
        return "M"
