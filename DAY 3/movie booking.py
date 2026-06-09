movies = {
    "M101": {"movie": "Leo", "theater": "PVR", "seats": 50, "price": 200},
    "M102": {"movie": "Jailer", "theater": "INOX", "seats": 40, "price": 180}
}

def book_movie():

    movie_name = input("Enter Movie Name: ")

    for movie_id, details in movies.items():

        if details["movie"].lower() == movie_name.lower():

            print("\nMovie Available")
            print("Movie ID:", movie_id)
            print("Theater:", details["theater"])
            print("Available Seats:", details["seats"])

            seats = int(input("How many tickets do you want? "))

            if seats <= details["seats"]:
                details["seats"] -= seats

                print("\nBooking Confirmed")
                print("Booked Tickets:", seats)
                print("Remaining Seats:", details["seats"])
            else:
                print("Not enough seats available")

            return

    print("Movie Not Available")

book_movie()
