class StringUtils:
    @staticmethod
    def is_blank(value):
        return value in (None, '') or not value.strip()
