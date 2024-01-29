from app.db.conn import engine
from sqlalchemy import text
import pytest


@pytest.mark.skip(reason="Connection succesfuly")
def test_connection_sqlite():
    with engine.connect() as conn:
        query = conn.execute(text("SELECT 'Hola, Mundo'"))

        result = query.all()

        assert isinstance(result, list)


@pytest.mark.skip(reason="Table test alredy exits")
def test_save_value():
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE test (x int, y int)"))
        conn.execute(
            text("INSERT INTO test (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )

        conn.commit()


@pytest.mark.skip(reason="Return value integer perfect")
def test_returns_value():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM test"))
        for row in result:
            assert isinstance(row.x, int)
            assert isinstance(row.y, int)
