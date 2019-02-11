class Notes:
    def __init__(self, n):
        secs = n.split(":")
        if len(secs) != 6:
            raise Exception("SM file format needs six sections")

        # Type, Name, Difficulty, Rating
        self.type = secs[0].lstrip()
        self.name = secs[1].lstrip()
        self.difficulty = secs[2].lstrip()
        self.rating = secs[3].lstrip()

        try:
            self.rating = int(self.rating)
        except:
            raise Exception("Rating of chart %s:%s is not an integer" % (self.type, self.name))

        # Groove Radar
        self.groove = [float(g) for g in secs[4].lstrip().split(",")]

        # Width
        if self.type == "dance-single":
            self.width = 4
        elif self.type == "dance-double" or self.type == "dance-routine":
            self.width = 8
        else:
            raise Exception("Cannot determine width from type (%s)" % self.type)

        # Measures -> Layers:Notes
        self.layers = []
        raw_layers = "".join(secs[5].split()).split("&")
        for layer in raw_layers:
            measures = layer.split(",")
            notes = []

            for i in xrange(len(measures)):
                m = measures[i]
                if (len(m) % self.width) != 0:
                    raise Exception("Uneven number of notes in measure %d" % i)
                
                p = len(m) / self.width
                if p not in [4, 8, 12, 16, 24, 32, 48, 64, 192]:
                    raise Exception("Nonstandard note division (%d)" % p)

                for j in xrange(p):
                    n = m[self.width*j:self.width*j+self.width]
                    if n != "0" * self.width:
                        notes.append((round(4*i + 4*j/float(p), 3), n))
            self.layers.append(notes)

            # TODO: Freezes

        # For backwards compatibility and simplicity with single-layer charts, provide self.notes
        self.notes = self.layers[0]

    def barf(self, LF="\r\n", mc=1):
        s  = LF
        s += "     %s:" % self.type + LF
        s += "     %s:" % self.name + LF
        s += "     %s:" % self.difficulty + LF
        s += "     %d:" % self.rating + LF
        s += "     %s:" % (",".join(["%0.3f" % g for g in self.groove])) + LF

        F = [48, 24, 16, 12, 8, 6, 4, 3, 1]
        for li in xrange(len(self.layers)):
            if li > 0: s += "&" + LF

            layer = self.layers[li]
            b = i = 0
            while i < len(layer):
                if b > 0: s += ","
                s += "  // measure %d" % (b/4+mc) + LF

                measure = dict()
                h = 48
                j = i
                while j < len(layer) and layer[j][0] < b+4:
                    x = round(layer[j][0] * 48)
                    for d in F:
                        if x % d == 0:
                            for g in F:
                                if x % g == 0 and h % g == 0:
                                    h = g
                                    break
                            break
                    measure.update([(x % 192, layer[j][1])])
                    j += 1
                for k in xrange(0, 192, h):
                    if k in measure:
                        s += measure[k] + LF
                    else:
                        s += "0" * self.width + LF

                i = j
                b += 4
        return s
