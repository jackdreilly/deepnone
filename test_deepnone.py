from deepnone import dn


def test_deepnone():
    assert dn(1).get == 1
    assert dn("ASDF").lower().get == "asdf"
    assert dn(123).lower().get is None
    assert dn(123).lower().default("hi") == "hi"
    assert dn("ASDF").strip("F").get == "ASD"
    assert dn("").junk().get is None
    assert dn(3).real.get == 3
    assert dn({"asdf": ["a", "b", "c"]})["asdf"][1].get == "b"
    assert dn({"asdf": ["a", "b", "c"]})["asdf"][1].upper().get == "B"
    assert dn({"asdf": ["a", "b", "c"]})["fdas"][1].upper().get is None
    assert dn(3).fn(str).get == "3"
    assert dn({"a": "b"}).attr("get")("a").get == "b"
    assert dn(123).junk.fn(str).get is None
    assert dn(123).fn(str)
    assert not dn(123).fn(str).junk
    assert bool(dn(123).fn(str))
    assert not bool(dn(123).fn(str).junk.asdf)
    assert list(dn(1).junk) == []
    for x in dn({"x": [3]})["x"]:
        assert x == 3
    assert not any(dn("a").junk)
    assert any(dn([1]))
    assert dn("a") == "a"
    assert "a" == dn("a")
    assert dn("a").upper() == "A"
