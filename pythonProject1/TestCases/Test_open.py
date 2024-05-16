import pytest
import softest
import pytest

@pytest.mark.usefixtures("SetUp")
class TestOpenWeb(softest.TestCase):
    def test_web(self):
        #Start writting your test cases from here
     self.soft_assert(self.assertEqual, 1, 2) #soft assertion for multiple assertion
     self.soft_assert(self.assertEqual, 2 , 2)
     self.soft_assert(self.assertEqual, 2 , 2)
     self.assert_all()