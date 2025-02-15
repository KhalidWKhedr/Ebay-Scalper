class Converter:
    @staticmethod
    def safe_int_conversion(value, default=None):
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
