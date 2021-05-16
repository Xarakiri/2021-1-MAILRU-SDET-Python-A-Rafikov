from collections import Counter

from sqlalchemy.orm import Session

import script
from mysql.models import LargestRequests
from mysql.models import MostFrequentRequests
from mysql.models import RequestsPerType
from mysql.models import TotalNumberOfRequests
from mysql.models import Users5xx


class Test:
    def test_count(self, client: Session):
        count = script.count_lines()
        res = TotalNumberOfRequests(total_count=count)
        client.add(res)
        client.commit()

        res = client.query(TotalNumberOfRequests).first()
        assert res.total_count == count

    def test_count_by_methods(self, client: Session):
        data = Counter(script.count_by_methods())
        for i, v in data.items():
            r = RequestsPerType(type=i, requests=v)
            client.add(r)
        client.commit()

        assert len(client.query(RequestsPerType).all()) == 5

    def test_top10(self, client: Session):
        data = Counter(script.top10()).most_common(10)
        for i in data:
            r = MostFrequentRequests(url=i[0], count=i[1])
            client.add(r)
        client.commit()

        assert len(client.query(MostFrequentRequests).all()) == 10

    def test_top5_by_bytes(self, client: Session):
        data = script.top5_by_bytes()
        for i in data:
            r = LargestRequests(
                url=i[0],
                status=i[1],
                size=i[2],
                ip=i[3]
            )
            client.add(r)
        client.commit()

        assert len(client.query(LargestRequests).all()) == 5

    def test_top5_by_5xx(self, client: Session):
        data = Counter(script.top5_by_5xx()).most_common(5)
        for i in data:
            r = Users5xx(ip=i[0], count=i[1])
            client.add(r)
        client.commit()

        assert len(client.query(Users5xx).all()) == 5
