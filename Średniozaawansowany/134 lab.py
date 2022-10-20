import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert  len(self.title) > 0,  "Title is empty!"
        assert self.start >= self.end, "Start date is later than end date!"


    @classmethod
    def publish_offer(cls,trips):
        list_of_errors = []
        for t in trips:
            try:
                t.check_data()
            except Exception as e:
                list_of_errors.append(f'symbol: {t.symbol}, ERROR: {e}')

        assert len(list_of_errors) == 0, f'The list of trips has errors: {list_of_errors}'


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Checking trips...')
    Trip.publish_offer(trips)
    print('DONE')
except Exception as e:
    print('ERROR!!!!!!!!!!!!!!!!',e)