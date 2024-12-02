from library_item import LibraryItem
import track_library as trlb


def test_libra (capsys, name, artist, rating=0):
    assert capsys.read