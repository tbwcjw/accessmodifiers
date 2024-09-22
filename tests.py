import unittest
from access import public_class, protected_class, private_class, public, protected, private

class TestAccessControl(unittest.TestCase):

    @public_class
    class PublicClass:
        @public
        def public_method(self):
            return "public"

        @protected
        def protected_method(self):
            return "protected"

        @private
        def private_method(self):
            return "private"

        @public
        def call_private_method(self):
            return self.private_method()

    @protected_class
    class ProtectedClass:
        @protected
        def protected_method(self):
            return "protected"

    @private_class
    class PrivateClass:
        @private
        def private_method(self):
            return "private"

    def test_public_method_access(self):
        obj = self.PublicClass()
        self.assertEqual(obj.public_method(), "public")

    def test_protected_method_access_in_subclass(self):
        class SubClass(self.ProtectedClass):
            def access_protected(self):
                return self.protected_method()

        obj = SubClass()
        self.assertEqual(obj.access_protected(), "protected")

    def test_protected_method_access_outside_class(self):
        with self.assertRaises(AttributeError):
            obj = self.ProtectedClass().protected_method()

    def test_private_method_access_outside_class(self):
        with self.assertRaises(AttributeError):
            obj = self.PrivateClass().private_method()

    def test_protected_class_instantiation(self):
        with self.assertRaises(AttributeError):
            self.ProtectedClass()

    def test_private_class_instantiation(self):
        with self.assertRaises(AttributeError):
            self.PrivateClass()

    def test_subclass_private_method_access(self):
        class SubPrivateClass(self.PrivateClass):
            def access_private(self):
                return self.private_method()

        obj = SubPrivateClass()
        with self.assertRaises(AttributeError):
            obj.access_private()

if __name__ == "__main__":
    unittest.main()