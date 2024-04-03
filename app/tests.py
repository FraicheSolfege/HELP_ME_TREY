from django.test import SimpleTestCase

# Create your tests here.


class TestCase(SimpleTestCase):
    def test_input_returns_true(self):
        response = self.client.get("/enter-num/93")
        print("hey")
        print(response)
        self.assertContains(response, True)

    def test_input_returns_false(self):
        response = self.client.get("/enter-num/88")
        print("hey")
        print(response)
        self.assertContains(response, False)
