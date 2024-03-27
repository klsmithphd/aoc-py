"""Utility functions for dealing with cryptographic hash digests"""
import hashlib


def md5_digest(s: str):
    """MD5 digest (as bytes) of the supplied string"""
    return hashlib.md5(s.encode()).digest()


def isfivezerostart(digest: bytes):
    """Does the supplied digest start with 5 zeros"""
    return digest[:3] < b'\x00\x00\x10'


def issixzerostart(digest: bytes):
    """Does the supplied diggest start with 6 zeros"""
    return digest[:3] == b'\x00\x00\x00'
