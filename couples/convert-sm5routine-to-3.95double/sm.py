from params import *
from notes import *

class SMError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class SM:
    def __init__(self, sm_file):
        self.filename = sm_file
        self.params = Params()
        self.bpms = []
        self.stops = []
        self.offset = 0.0

        self.parse_sm(sm_file)

    def parse_sm(self, sm_file):
        try:
            sm_raw = open(sm_file, "rb").read()
        except:
            raise SMError("Cannot open \"%s\"" % sm_file)

        # Convert to UNIX format
        sm_raw = sm_raw.replace("\r\n", "\n")
        sm_raw = sm_raw.replace("\r", "\n")

        # Remove comments
        while True:
            i = sm_raw.find("//")
            if i == -1:
                break

            j = sm_raw.find("\n", i)
            if j == -1:
                sm_raw = sm_raw[:i]
            else:
                sm_raw = sm_raw[:i] + sm_raw[j:]

        # Create params dictionary
        params = Params()
        i = 0
        while i < len(sm_raw):
            i = sm_raw.find("#", i)
            j = sm_raw.find(";", i+1)
            if i == -1:
                break
            if j == -1:
                line = sm_raw[i+1:]
            else:
                line = sm_raw[i+1:j]

            k = line.find(":")
            if k == -1:
                raise SMError("Pound-colon syntax broken")
            params.add(line[:k], line[k+1:])
            i = j + 1

        self.params = params

        # Grab BPMS/STOPS
        self.parse_bpms()
        self.parse_stops()

        # Grab NOTES
        self.parse_notes()

        self.offset = float(self.params["OFFSET"][0]) # TODO

    def parse_bpms(self):
        bpms = self.params["BPMS"]
        if len(bpms) != 1:
            raise SMError("SM should have exactly one #BPMS line")
        bpms = SM.parse_list(bpms[0])
        if len(bpms) < 1:
            raise SMError("SM should have at least one BPM defined")
        bpms = SM.list_use_nums(bpms)
        if bpms[0][0] != 0:
            raise SMError("First BPM should be at position 0")
        self.bpms = bpms

    def parse_stops(self):
        stops = self.params["STOPS"]
        if len(stops) != 1:
            raise SMError("SM should have exactly one #STOPS line")
        stops = SM.parse_list(stops[0])
        self.stops = SM.list_use_nums(stops)

    def parse_notes(self):
        notes = []
        for n in self.params["NOTES"]:
            notes.append(Notes(n))
        self.notes = notes

    def barf(self, LF="\r\n", mc=1):
        plist = ["TITLE", "SUBTITLE", "ARTIST", "TITLETRANSLIT", "SUBTITLETRANSLIT", "ARTISTTRANSLIT", "GENRE", "CREDIT", "BANNER", "BACKGROUND", "LYRICSPATH", "CDTITLE", "MUSIC", "OFFSET", "SAMPLESTART", "SAMPLELENGTH", "SELECTABLE", "DISPLAYBPM", "BPMS", "STOPS", "FGCHANGES", "BGCHANGES", "BGCHANGES2", "KEYSOUNDS"]
        pinvis = set(["SAMPLESTART", "SAMPLELENGTH", "SELECTABLE", "DISPLAYBPM", "BGCHANGES2"])
        pleft = set([k for k,v in self.params])
        try: pleft.remove("NOTES")
        except: pass

        s = ""
        while len(pleft) > 0:
            try:
                while True:
                    item = plist.pop(0)
                    if not item in self.params and item in pinvis: continue
                    break
                if item in pleft: pleft.remove(item)
            except:
                item = pleft.pop()
            if item == "BPMS":
                s += "#%s:" % item
                for i in xrange(len(self.bpms)):
                    if i > 0: s += ","
                    (a,b) = self.bpms[i]
                    s += "%.3f=%.3f" % (a, b) + LF
                s += ";" + LF
            elif item == "STOPS": # merge with above
                s += "#%s:" % item
                for i in xrange(len(self.stops)):
                    if i > 0: s += ","
                    (a,b) = self.stops[i]
                    s += "%.3f=%.3f" % (a, b) + LF
                s += ";" + LF
            elif item == "OFFSET":
                s += "#%s:%.3f;" % (item, self.offset) + LF
            else:
                for value in self.params[item]:
                    s += "#%s:%s;" % (item, value) + LF

        for notes in self.notes:
            s += LF
            s += "//---------------%s - %s----------------" % (notes.type, notes.name) + LF
            s += "#NOTES:" + notes.barf(LF, mc) + ";" + LF

        s += LF
        return s

    # Static Methods

    @staticmethod
    def list_use_nums(ls):
        new = []
        for a,b in ls:
            new.append((float(a), float(b)))
        return new

    @staticmethod
    def parse_list(ls):
        ls = "".join(ls.split("\n"))
        ls = "".join(ls.split())
        if ls == "": return []

        ls = ls.split(",")
        pairs = []
        for i in xrange(len(ls)):
            p = ls[i].split("=")
            if len(p) != 2:
                raise Exception("Bad list formatting")
            pairs.append((p[0], p[1]))
        return pairs
