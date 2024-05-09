class MovieTicketChatbot:
    def __init__(self):
        self.movies = {
            "Inception": {
                "times": ["2:00 PM", "5:00 PM", "8:00 PM"],
                "price": 10.00,
            },
            "Avengers: Endgame": {
                "times": ["1:00 PM", "4:00 PM", "7:00 PM"],
                "price": 12.00,
            },
            "The Matrix": {
                "times": ["3:00 PM", "6:00 PM", "9:00 PM"],
                "price": 8.00,
            },
        }
        self.booked_tickets = []

    def greet(self):
        print("Hello! Welcome to the movie ticket counter chatbot.")
        print("How can I assist you today?")

    def show_available_movies(self):
        print("Here are the available movies and showtimes:")
        for movie, details in self.movies.items():
            times = ", ".join(details["times"])
            print(f"{movie}: {times}")

    def book_ticket(self):
        movie_name = input("Enter the name of the movie you want to book tickets for: ")
        if movie_name in self.movies:
            print(f"Available showtimes for {movie_name}:")
            times = ", ".join(self.movies[movie_name]["times"])
            print(times)
            time = input("Enter the showtime you want to book: ")
            if time in self.movies[movie_name]["times"]:
                ticket_id = len(self.booked_tickets) + 1
                seat_no = input("Enter the seat number: ")
                price = self.movies[movie_name]['price']
                self.booked_tickets.append({"ticket_id": ticket_id, "movie_name": movie_name, "time": time, "seat_no": seat_no, "price": price})
                print(f"Ticket booked successfully!\nTicket ID: {ticket_id}, Movie: {movie_name}, Time: {time}, Seat No: {seat_no}, Price: ${price}")
            else:
                print("Sorry, that showtime is not available.")
        else:
            print("Sorry, that movie is not available.")

    def confirm_ticket(self, ticket_id):
        for ticket in self.booked_tickets:
            if ticket["ticket_id"] == ticket_id:
                print(f"Confirmed Ticket Details:\nTicket ID: {ticket['ticket_id']}, Movie: {ticket['movie_name']}, Time: {ticket['time']}, Seat No: {ticket['seat_no']}, Price: ${ticket['price']}")
                return
        print("Ticket not found.")

    def cancel_ticket(self, ticket_id):
        for ticket in self.booked_tickets:
            if ticket["ticket_id"] == ticket_id:
                self.booked_tickets.remove(ticket)
                print(f"Ticket {ticket_id} canceled successfully.")
                return
        print("Ticket not found.")

    def run(self):
        self.greet()
        while True:
            user_input = input("Enter '1' to see available movies, '2' to book a ticket, '3' to confirm a ticket, '4' to cancel a ticket, or 'quit' to exit: ").strip()
            if user_input == '1':
                self.show_available_movies()
            elif user_input == '2':
                self.book_ticket()
            elif user_input == '3':
                ticket_id = int(input("Enter the ticket ID to confirm: "))
                self.confirm_ticket(ticket_id)
            elif user_input == '4':
                ticket_id = int(input("Enter the ticket ID to cancel: "))
                self.cancel_ticket(ticket_id)
            elif user_input.lower() == 'quit':
                print("Thank you! Have a great day!")
                break
            else:
                print("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    chatbot = MovieTicketChatbot()
    chatbot.run()
