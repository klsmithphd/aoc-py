import utils.digest as dig


def test_md5_digest():
    assert dig.md5_digest('abcdef') == \
        b'\xe8\x0b\x50\x17\x09\x89\x50\xfc\x58\xaa\xd8\x3c\x8c\x14\x97\x8e'


def test_isfivezerostart():
    assert True == dig.isfivezerostart(b'\x00\x00\x01\xff')  # 000001ff
    assert False == dig.isfivezerostart(b'\x00\x00\x10\xff')  # 000010ff


def test_issixzerostart():
    assert True == dig.issixzerostart(b'\x00\x00\x00\xff')  # 000000ff
    assert False == dig.issixzerostart(b'\x00\x00\x01\xff')  # 000001ff
