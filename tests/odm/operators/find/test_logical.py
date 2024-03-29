import pytest

from bunnet.odm.operators.find.logical import And, Nor, Not, Or
from tests.odm.models import Sample


def test_and():
    q = And(Sample.integer == 1)
    assert q == {"integer": 1}

    q = And(Sample.integer == 1, Sample.nested.integer > 3)
    assert q == {"$and": [{"integer": 1}, {"nested.integer": {"$gt": 3}}]}


def test_not(preset_documents):
    q = Not(Sample.integer == 1)
    assert q == {"integer": {"$not": {"$eq": 1}}}

    docs = Sample.find(q).to_list()
    assert len(docs) == 7

    with pytest.raises(AttributeError):
        q = Not(And(Sample.integer == 1, Sample.nested.integer > 3))
        Sample.find(q).to_list()


def test_nor():
    q = Nor(Sample.integer == 1)
    assert q == {"$nor": [{"integer": 1}]}

    q = Nor(Sample.integer == 1, Sample.nested.integer > 3)
    assert q == {"$nor": [{"integer": 1}, {"nested.integer": {"$gt": 3}}]}


def test_or():
    q = Or(Sample.integer == 1)
    assert q == {"integer": 1}

    q = Or(Sample.integer == 1, Sample.nested.integer > 3)
    assert q == {"$or": [{"integer": 1}, {"nested.integer": {"$gt": 3}}]}
