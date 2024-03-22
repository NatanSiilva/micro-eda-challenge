import unittest
from src.application.shared.validator import ValidatorRoles
from src.application.shared.exception import ValidationException


class TestValidatorRoles(unittest.TestCase):

    def test_values_method(self):
        validator = ValidatorRoles.values("some value", "prop")

        self.assertIsInstance(validator, ValidatorRoles)
        self.assertEqual(validator.value, "some value")
        self.assertEqual(validator.prop, "prop")


    def test_required_rule(self):
        invalid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "", 'prop': 'prop'}
        ]

        for i in invalid_data:
            msg=f"value: {i['value'], {i['prop']}}"

            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRoles.values(i["value"] , i["prop"]).required(),
            
            self.assertEqual(
                "The prop is required", 
                assert_error.exception.args[0]   
            )

        valid_data = [
            {'value': "test", 'prop': 'prop'},
            {'value': 5, 'prop': 'prop'},
            {'value': 0, 'prop': 'prop'},
            {'value': False, 'prop': 'prop'}
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRoles.values(i["value"] , i["prop"]).required(),
                ValidatorRoles
            )
    

    def test_string_rule(self):
        invalid_data = [
            {'value': 5, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'}
        ]

        for i in invalid_data:
            msg=f"value: {i['value'], {i['prop']}}"

            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRoles.values(i["value"] , i["prop"]).string(),
            
            self.assertEqual(
                "The prop must be a string", 
                assert_error.exception.args[0]   
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': "some value", 'prop': 'prop'},
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRoles.values(i["value"] , i["prop"]).string(),
                ValidatorRoles
            )


    def test_integer_rule(self):
        invalid_data = [
            {'value': 5.1, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': "test", 'prop': 'prop'}
        ]

        for i in invalid_data:
            msg=f"value: {i['value'], {i['prop']}}"

            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRoles.values(i["value"] , i["prop"]).integer(),
            
            self.assertEqual(
                "The prop must be an integer", 
                assert_error.exception.args[0]   
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': 1, 'prop': 'prop'},
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRoles.values(i["value"] , i["prop"]).integer(),
                ValidatorRoles
            )


    def test_max_length_rule(self):
        invalid_data = [
            {'value': "t" * 5, 'prop': 'prop'},
        ]

        for i in invalid_data:
            msg=f"value: {i['value'], {i['prop']}}"

            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRoles.values(i["value"] , i["prop"]).max_length(4),
            
            self.assertEqual(
                "The prop must be less than 4 characters", 
                assert_error.exception.args[0]   
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': "t" * 5, 'prop': 'prop'}
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRoles.values(i["value"] , i["prop"]).max_length(5),
                ValidatorRoles
            )


    def test_boolean_rule(self):
        invalid_data = [
            {'value': "t" * 5, 'prop': 'prop'},
            {'value': "", 'prop': 'prop'},
            {'value': 5, 'prop': 'prop'},
            {'value': {}, 'prop': 'prop'},
        ]

        for i in invalid_data:
            msg=f"value: {i['value'], {i['prop']}}"

            with self.assertRaises(ValidationException, msg=msg) as assert_error:
                ValidatorRoles.values(i["value"] , i["prop"]).boolean(),
            
            self.assertEqual(
                "The prop must be a boolean", 
                assert_error.exception.args[0]   
            )

        valid_data = [
            {'value': None, 'prop': 'prop'},
            {'value': True, 'prop': 'prop'},
            {'value': False, 'prop': 'prop'}
        ]

        for i in valid_data:
            self.assertIsInstance(
                ValidatorRoles.values(i["value"] , i["prop"]).boolean(),
                ValidatorRoles
            )


    def test_throw_a_validation_exception_when_combine_two_or_more_roles(self):
        with self.assertRaises(ValidationException) as assert_error:
            ValidatorRoles.values(None, "prop").required().string().max_length(5)
        
        self.assertEqual(
            "The prop is required", 
            assert_error.exception.args[0]   
        )

        with self.assertRaises(ValidationException) as assert_error:
            ValidatorRoles.values(5, "prop").required().string().max_length(5)
        
        self.assertEqual(
            "The prop must be a string", 
            assert_error.exception.args[0]   
        )


        with self.assertRaises(ValidationException) as assert_error:
            ValidatorRoles.values("t" * 5, "prop").required().string().max_length(4)
        
        self.assertEqual(
            "The prop must be less than 4 characters", 
            assert_error.exception.args[0]   
        )

        with self.assertRaises(ValidationException) as assert_error:
            ValidatorRoles.values(None, "prop").required().boolean()
        
        self.assertEqual(
            "The prop is required", 
            assert_error.exception.args[0]   
        )

        with self.assertRaises(ValidationException) as assert_error:
            ValidatorRoles.values(5, "prop").required().boolean()
        
        self.assertEqual(
            "The prop must be a boolean", 
            assert_error.exception.args[0]   
        )

        with self.assertRaises(ValidationException) as assert_error:
            ValidatorRoles.values(1.0, "prop").required().integer()

        self.assertEqual(
            "The prop must be an integer", 
            assert_error.exception.args[0]   
        )
    
    def test_valid_cases_for_combination_between_rules(self):
        ValidatorRoles.values("test", "prop").required().string()
        ValidatorRoles.values("t" * 5, "prop").required().string().max_length(5)

        ValidatorRoles.values(True, "prop").required().boolean()
        ValidatorRoles.values(False, "prop").required().boolean()

        ValidatorRoles.values(11, "prop").required().integer()
        self.assertTrue(True)
