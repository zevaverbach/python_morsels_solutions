class Date:

    def __init__(self, date_string):
        self.month, self.day, self.year = map(int, date_string.split('/'))

    def __str__(self):
        return f'{self.month:02}/{self.day:02}/{self.year}'

    def __lt__(self, other):
        for attr in ['year', 'month', 'day']:
            if getattr(self, attr) == getattr(other, attr):
                continue
            return getattr(self, attr) < getattr(other, attr)
        return False


def get_earliest(*date_strings):
    return str(min(map(Date, date_strings)))
