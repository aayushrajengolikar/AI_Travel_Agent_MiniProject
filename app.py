from tools.ollama_tool import generate_travel_plan
import streamlit as st
from tools.weather_tool import get_weather
from tools.ollama_tool import generate_travel_plan
from tools.places_tool import get_tourist_places
from tools.hotel_tool import get_hotels
from tools.flights_tool import get_flight_routes
from tools.budget_tool import estimate_budget

st.title("AI Travel Planner")

# User Inputs
source = st.text_input("Source City")
destination = st.text_input("Destination City")

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

travellers = st.number_input("Number of Travellers", min_value=1, max_value=10, value=1)

interests = st.text_input("Interests (food, history, nature, shopping, etc.)")


# Generate Travel Plan
if st.button("Generate Travel Plan"):

    if destination.strip() == "":
        st.warning("Please enter a destination city")

    else:
        st.write("Planning your trip...")

        # Weather
        weather_data = get_weather(destination)

        st.subheader("Weather Forecast Data")
        st.json(weather_data)

        # Tourist places
        places = get_tourist_places(destination)

        st.subheader("Tourist Places (Real Map Data)")
        st.write(places)

        # Hotels
        hotels = get_hotels(destination)

        st.subheader("Hotel Suggestions")
        st.write(hotels)

        # Flights
        flights = get_flight_routes(source, destination)

        st.subheader("Flight Routes")
        st.write(flights)

        # Budget estimation
        budget = estimate_budget(destination, start_date, end_date, travellers)

        st.subheader("Estimated Travel Budget")
        st.json(budget)

        # Prompt for LLM
        prompt = f"""
You are an AI travel planner.

Create a travel itinerary using the following information.

Source: {source}
Destination: {destination}
Start Date: {start_date}
End Date: {end_date}
Number of Travellers: {travellers}
Interests: {interests}

Weather Data:
{weather_data}

Tourist Places:
{places}

Hotels:
{hotels}

Flights:
{flights}

Budget Estimate:
{budget}

Create a well structured travel plan including:

1. Flight suggestions
2. Hotel recommendations
3. A travel itinerary using the tourist places provided
4. Weather summary
5. Budget breakdown and tips to save money
"""

        st.write("Generating AI travel plan...")

        try:
            travel_plan = generate_travel_plan(prompt)

            st.subheader("AI Travel Plan")

            if travel_plan:
                st.markdown(travel_plan)
            else:
                st.error("No response received from the model.")

        except Exception as e:
            st.error(f"Ollama Error: {e}")