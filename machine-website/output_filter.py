from os import linesep

def basic_filter(output_str):
    # separate string output by line, essentially, by entry
    pre_songs = output_str.split(linesep)

    # keep only folder names
    only_folders = filter(lambda song : '.' not in song, pre_songs)

    return only_folders