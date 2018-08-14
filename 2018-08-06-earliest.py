

class Date:

    def __init__(self, date_string):
        self.month, self.day, self.year = split_date_string(date_string)

    def __str__(self):
        return f'{self.month:02}/{self.day:02}/{self.year}'

    def __lt__(self, other):
        for attr in ['year', 'month', 'day']:
            if getattr(self, attr) < getattr(other, attr):
                return True
            elif getattr(self, attr) > getattr(other, attr):
                return False


def get_earliest(*date_strings):
    dates = [Date(date_string) for date_string in date_strings]
    return str(min(dates))


def split_date_string(date_string):
    month, day, year = date_string.split('/')
    return int(month), int(day), int(year)
