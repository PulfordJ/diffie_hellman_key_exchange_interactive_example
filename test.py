import unittest
import diffie_hellman

class TestDiffieHellman(unittest.TestCase):
    """
    See https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
    for more information.
    """

    def test_encrypt_integer(self):
        """
        This output is what is often sent unencrypted.
        """
        self.assertEqual(diffie_hellman.encrypt_integer(5, 23, 3), 10)
        self.assertEqual(diffie_hellman.encrypt_integer(5, 23, 4), 4)

    
    def test_shared_secret_is_equal(self):
        """
        Once the recipient has the output from the above test
        This is how a symmetric key can be formed securely.
        Both sides now have the same password, without ever sharing one
        in an unencrypted format.
        """
        self.assertEqual(
                diffie_hellman.encrypt_integer(diffie_hellman.encrypt_integer(5, 23, 4), 23, 3), 
                diffie_hellman.encrypt_integer(diffie_hellman.encrypt_integer(5, 23, 3), 23, 4),
                18 #The new shared key.
                )
        self.assertEqual(
                diffie_hellman.encrypt_integer(diffie_hellman.encrypt_integer(5, 23, 14), 23, 17),
                diffie_hellman.encrypt_integer(diffie_hellman.encrypt_integer(5, 23, 17), 23, 14),
                2 #The new shared key.
                )

    def test_brute_force_secret_is_equal(self):
        """
        This checks all possible combinations of keys given the prime 23.
        """
        self.assertEqual(diffie_hellman.encrypt_integer(5, 23, 3), 10)
        self.assertEqual(diffie_hellman.encrypt_integer(5, 23, 4), 4)
        g = 5
        p = 23

        for i in range (0, p):
            for j in range (0, p):
                shared1 = diffie_hellman.encrypt_integer(diffie_hellman.encrypt_integer(g, p, i), p, j)
                shared2 = diffie_hellman.encrypt_integer(diffie_hellman.encrypt_integer(g, p, j), p, i)
                self.assertEqual(shared1, shared2)

if __name__ == '__main__':
    unittest.main()
