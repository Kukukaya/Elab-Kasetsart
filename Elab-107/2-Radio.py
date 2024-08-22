class Radio():
    def __init__(rad,mode = 'FM',frequency = 87.5):
        rad.mode = mode
        rad.frequency = frequency

    def __str__(rad):
        if rad.get_mode() == 'FM':
            return f"F{rad.get_mode()} Radio: {rad.get_frequency():.1f} MHz"
        elif rad.get_mode() == 'AM':
            return f"F{rad.get_mode()} Radio: {rad.get_frequency():.1f} kHz"

    def set_mode(rad,mode):
        rad.mode = mode
        if rad.get_mode() == 'FM':
            rad.frequency = 87.5
        elif rad.get_mode() == 'AM':
            rad.frequency = 150

    def set_frequency(rad,frequency):
        if rad.get_mode() == 'FM':
            if rad.get_frequency() >= 87.5 and rad.get_frequency() <= 108:
                rad.frequency = frequency
        elif rad.get_mode() == 'AM':
            if rad.get_frequency() >= 150 and rad.get_frequency() <= 280:
                rad.frequency = frequency

    def adjust_frequency(rad,frequency):
        if rad.get_mode() == 'FM':
            if rad.frequency + frequency >= 87.5 and rad.frequency + frequency <= 108:
                rad.frequency += frequency
                return True
        elif rad.get_mode() == 'AM':
            if rad.frequency + frequency >= 150 and rad.frequency + frequency <= 280:
                rad.frequency += frequency
                return True
        return False

    def get_mode(rad):
        return rad.mode
    def get_frequency(rad):
        return rad.frequency
