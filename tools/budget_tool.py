def estimate_budget(destination, start_date, end_date, travellers):

    # Calculate number of days
    trip_days = (end_date - start_date).days
    if trip_days <= 0:
        trip_days = 1

    # Estimated costs (simple averages)
    flight_cost_per_person = 300
    hotel_cost_per_night = 120
    food_cost_per_day = 40
    transport_cost_per_day = 20
    attraction_cost_per_day = 25

    # Calculations
    flights_total = flight_cost_per_person * travellers
    hotel_total = hotel_cost_per_night * trip_days
    food_total = food_cost_per_day * travellers * trip_days
    transport_total = transport_cost_per_day * travellers * trip_days
    attraction_total = attraction_cost_per_day * travellers * trip_days

    total_cost = flights_total + hotel_total + food_total + transport_total + attraction_total

    budget_data = {
        "destination": destination,
        "trip_days": trip_days,
        "travellers": travellers,
        "flight_estimate": flights_total,
        "hotel_estimate": hotel_total,
        "food_estimate": food_total,
        "transport_estimate": transport_total,
        "attractions_estimate": attraction_total,
        "total_estimated_budget": total_cost
    }

    return budget_data