import utils.digest as digest


def test_md5_digest():
    assert digest.md5_digest('abcdef') == \
        b'\xe8\x0b\x50\x17\x09\x89\x50\xfc\x58\xaa\xd8\x3c\x8c\x14\x97\x8e'


def test_isfivezerostart():
    assert True == digest.isfivezerostart(b'\x00\x00\x01\xff')  # 000001ff
    assert False == digest.isfivezerostart(b'\x00\x00\x10\xff')  # 000010ff


def test_issixzerostart():
    assert True == digest.issixzerostart(b'\x00\x00\x00\xff')  # 000000ff
    assert False == digest.issixzerostart(b'\x00\x00\x01\xff')  # 000001ff
