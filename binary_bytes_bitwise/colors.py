class Colors:
    def __init__(self, rgb: hex = None):
        self.rgb = rgb

    def get_red(self):
        return self.rgb >> 16

    def get_blue(self):
        return (self.rgb & 0x00ff00) >> 8

    def get_green(self):
        return self.rgb & 0xff

    def from_rgb(self, red, blue, green):
        self.rgb = (red << 16) | (blue << 8) | green


mona = Colors(0x7f8053)
# mona = Colors(8355923)
print(f"Colors of Mona Lisa: R={mona.get_red()}, G={mona.get_green()}, B={mona.get_blue()}")

lisa = Colors()
lisa.from_rgb(red=mona.get_red(), blue=mona.get_blue(), green=mona.get_green())

print(mona.rgb == lisa.rgb)
