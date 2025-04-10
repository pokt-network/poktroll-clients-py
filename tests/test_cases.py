from pocket_clients.cases import camel_to_snake_case


def test_camel_to_snake_case():
    assert camel_to_snake_case("CamelCase") == "camel_case"
    assert camel_to_snake_case("CamelCaseWithACapitalLetter") == "camel_case_with_a_capital_letter"
    assert camel_to_snake_case("CamelCaseWithAn_Underscore") == "camel_case_with_an__underscore"
    assert camel_to_snake_case("CamelCaseWithAn_UnderscoreAndACapitalLetter") == "camel_case_with_an__underscore_and_a_capital_letter"