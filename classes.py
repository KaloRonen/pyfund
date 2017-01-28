class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No ailrline code in '{0}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid ailrline code '{0}'".format(number))
        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError("Invalid rout number '{0}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number


    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        row = seat[:-1]

        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        try:
            row_num = int(row)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row))

        if row_num not in rows:
            raise ValueError("Invalid row number".format(row_num))

        return row_num, letter


    def allocate_seat(self, seat, passanger):
        row_num, letter = self._parse_seat(seat)

        if self._seating[row_num][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row_num][letter] = passanger


    def relocate_passanger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passanger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)

        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat('12A', 'ronenk')
    f.allocate_seat('15F', 'eyalsi')
    f.allocate_seat('15E', 'cimir')
    f.allocate_seat('1C', 'igalb')
    f.allocate_seat('1D', 'annakr')
    return f
