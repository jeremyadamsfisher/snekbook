<<<<<<< HEAD
import unittest as ut
import django.test as dj
from django.test import Client
from django.urls import reverse
=======
from django.test import TestCase
from django.contrib.auth import get_user_model
>>>>>>> a1a171b23d75b015c92310c839ef2e9354d4046d

from .utils import translation

<<<<<<< HEAD

class Translation(ut.TestCase):
    def test_translate(self):
        # fmt: off
        for eng, snek in [
                ("hellote", "sssssss"),
                ("Hellote", "Sssssss"),
                ("Hellote!", "Sssssss!"),
                (
                    """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

                    Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

                    But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.""",
                    """Ssss sssss sss sssss sssss sss sss sssssss sssssss sssss ss ssss sssssssss, s sss ssssss, sssssssss ss Sssssss, sss sssssssss ss sss sssssssssss ssss sss sss sss sssssss sssss.

                    Sss ss sss sssssss ss s sssss sssss sss, sssssss sssssss ssss ssssss, ss sss ssssss ss sssssssss sss ss sssssssss, sss ssss ssssss. Ss sss sss ss s sssss ssssss-sssss ss ssss sss. Ss ssss ssss ss ssssssss s sssssss ss ssss sssss, ss s sssss sssssss sssss sss sssss sss ssss ssss sssss sssss ssss ssss ssssss sssss ssss. Ss ss ssssssssss sssssss sss ssssss ssss ss ssssss ss ssss.

                    Sss, ss s ssssss sssss, ss sss sss ssssssss -- ss sss sss ssssssssss -- ss sss sss ssssss -- ssss ssssss. Sss sssss sss, ssssss sss ssss, sss sssssssss ssss, ssss sssssssssss ss, sss sssss sss ssss sssss ss sss ss sssssss. Sss sssss ssss ssssss ssss, sss ssss ssssssss ssss ss sss ssss, sss ss sss sssss ssssss ssss ssss sss ssss. Ss ss sss ss sss ssssss, ssssss, ss ss sssssssss ssss ss sss ssssssssss ssss sssss ssss sss ssssss ssss ssss ssss sss ss sssss ssssssss. Ss ss ssssss sss ss ss ss ssss sssssssss ss sss sssss ssss sssssssss ssssss ss -- ssss ssss sssss sssssss ssss ss ssss sssssssss ssssssss ss ssss sssss sss sssss ssss ssss sss ssss ssss sssssss ss ssssssss -- ssss ss ssss ssssss sssssss ssss sssss ssss sssss sss ssss ssss ss ssss -- ssss ssss ssssss, sssss Sss, sssss ssss s sss sssss ss sssssss -- sss ssss ssssssssss ss sss ssssss, ss sss ssssss, sss sss ssssss, sssss sss ssssss ssss sss sssss.""",
                ),
            ]:
            with self.subTest():
                self.assertEqual(translation.to_snek(eng), snek)
        # fmt: on


class Index(dj.TestCase):
    def test_logged_in_view_shows_users_name(self):
        client = Client()
        response = client.get(reverse("home"))
        self.assertIs(response.status_code, 200)
=======
class SnekbookTests(TestCase):
    def test_test(self):
        self.assertEqual(1, 1)
>>>>>>> a1a171b23d75b015c92310c839ef2e9354d4046d
