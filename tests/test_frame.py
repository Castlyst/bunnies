from unittest import TestCase
import pandas as pd

from bunnies import DataFrame
from bunnies.cols import Column


class TestFrame(TestCase):
    def test_get_item(self):
        # Arrange
        df = DataFrame(pd.DataFrame([[1, 2, 3]], columns=["a", "b", "c"]))
        expected_get_one = Column("a")
        expected_get_two = pd.DataFrame([[1,2]], columns=["a", "b"])

        # Act
        result_get_one = df["a"]
        result_get_two = df[["a", "b"]]

        # Assert
        self.assertEqual(result_get_one, expected_get_one)
        pd.testing.assert_frame_equal(expected_get_two, result_get_two._frame)

    def test_get_attr(self):
        # Arrange
        df = DataFrame(pd.DataFrame([[1, 2, 3]], columns=["a", "b", "c"]))
        expected = Column("a")

        # Act
        result = df.a

        # Assert
        self.assertEqual(expected, result)