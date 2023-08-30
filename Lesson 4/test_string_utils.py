from string_utils import StringUtils
import pytest

stringUtils = StringUtils()


@pytest.mark.parametrize("string, res", [("", ""),
                                         (" ", " ")])
def test_negative_capitilize(string, res):
    text = stringUtils.capitilize(string)
    assert text == res


def test_negative_capitilize_none():
    with pytest.raises(TypeError):
        stringUtils.capitilize()


@pytest.mark.parametrize("string, res", [("тест", "Тест"),
                                         ("Test", "Test"),
                                         ("!@#$%", "!@#$%"),
                                         ("1234565677", "1234565677"),
                                         ("14 августа 2023", "14 августа 2023")])
def test_positive_capitilize(string, res):
    text = stringUtils.capitilize(string)
    assert text == res


def test_positive_capitilize_num():
    with pytest.raises(AttributeError):
        stringUtils.capitilize(12345)


@pytest.mark.parametrize("string, res", [("", ""),
                                         (" ", "")])
def test_negative_trim(string, res):
    text = stringUtils.trim(string)
    assert text == res


def test_negative_trim_none():
    with pytest.raises(TypeError):
        stringUtils.trim()


@pytest.mark.parametrize("str1, res", [("  тест", "тест"),
                                       (" Test", "Test"),
                                       ("         !@#$%", "!@#$%"),
                                       ("1234565677", "1234565677"),
                                       (" 14 августа 2023", "14 августа 2023")])
def test_positive_trim(str1, res):
    text = stringUtils.trim(str1)
    assert text == res


def test_positive_trim_num():
    with pytest.raises(AttributeError):
        stringUtils.trim(12345)


@pytest.mark.parametrize("string, res", [("", []),
                                         (" ", [])])
def test_negative_list(string, res):
    text = stringUtils.to_list(string)
    assert text == res


def test_negative_to_list():
    text = stringUtils.to_list(" : ", ":")
    assert text == [" ", " "]


def test_negative_to_list_none():
    with pytest.raises(TypeError):
        stringUtils.to_list()


@pytest.mark.parametrize("string, delimeter, res", [("1:2:3:4", ":", ["1", "2", "3", "4"]),
                                                    ("23 августа", " ", ["23", "августа"]),
                                                    ("@!#!$!%!^", "!", ["@", "#", "$", "%", "^"]),
                                                    ("Это строка с пробелами", " ", ["Это", "строка", "с", "пробелами"])
                                                    ])
def test_positive_to_list(string, delimeter, res):
    texst = stringUtils.to_list(string, delimeter)
    assert texst == res


def test_positive_list():
    texst = stringUtils.to_list("T,e,s,t")
    assert texst == ["T", "e", "s", "t"]


def test_to_list():
    with pytest.raises(TypeError):
        stringUtils.to_list(1, 2, 3, 4)


def test_negative_contains_none():
    with pytest.raises(TypeError):
        stringUtils.contains()


@pytest.mark.parametrize("string, symbol, res", [("", "u", False), (" ", " ", True)])
def test_negative_contains(string, symbol, res):
    text = stringUtils.contains(string, symbol)
    assert text == res


@pytest.mark.parametrize("string, symbol, res",
                         [("Text", "ex", True),
                          ("1:2:3:4", ":", True),
                          ("23 августа", " ", True),
                          ("Это строка с пробелами", "r", False)])
def test_positive_contains(string, symbol, res):
    text = stringUtils.contains(string, symbol)
    assert text == res


def test_contains():
    with pytest.raises(TypeError):
        stringUtils.contains(1, 2, 3, 4)


def test_negative_delete_symbol_none():
    with pytest.raises(TypeError):
        stringUtils.delete_symbol()


def test_negative_delete_symbol():
    text = stringUtils.delete_symbol(" ", " ")
    assert text == ""


@pytest.mark.parametrize("string, delete, res", [("Text", "ex", "Tt"),
                                                 ("Text", "", "Text"),
                                                 ("1:2:3:4", ":", "1234"),
                                                 ("23 августа", " ", "23августа"),
                                                 ("Это строка с пробелами", "r", "Это строка с пробелами")])
def test_positive_delete_symbol(string, delete, res):
    text = stringUtils.delete_symbol(string, delete)
    assert text == res


def test_delete_symbol():
    with pytest.raises(TypeError):
        stringUtils.delete_symbol(1, 2, 3, 4)


def test_negative_starts_with_none():
    with pytest.raises(TypeError):
        stringUtils.starts_with()


@pytest.mark.parametrize("string, starts, res", [("", "u", False),
                                                 (" ", " ", True)])
def test_negative_starts_with(string, starts, res):
    text = stringUtils.starts_with(string, starts)
    assert text == res


@pytest.mark.parametrize("string, starts, res", [("Text", "t", False),
                                                 ("Text", "", True),
                                                 ("1:2:3:4", "1", True),
                                                 ("23 августа", "2", True),
                                                 ("Это строка с пробелами", "Э", True)])
def test_positive_starts_with(string, starts, res):
    text = stringUtils.starts_with(string, starts)
    assert text == res


def test_starts_with():
    with pytest.raises(TypeError):
        stringUtils.starts_with(1, 2, 3, 4)


def test_negative_end_with_none():
    with pytest.raises(TypeError):
        stringUtils.end_with()


@pytest.mark.parametrize("string, end, res", [("", "u", False),
                                              (" ", " ", True)])
def test_negative_end_with(string, end, res):
    text = stringUtils.end_with(string, end)
    assert text == res


@pytest.mark.parametrize("string, end, res", [("Text", "t", True),
                                              ("Text", "", True),
                                              ("1:2:3:4", "`1", False),
                                              ("23 августа", "A", False),
                                              ("Это строка с пробелами", "Э", False)])
def test_positive_end_with(string, end, res):
    text = stringUtils.end_with(string, end)
    assert text == res


def test_end_with():
    with pytest.raises(TypeError):
        stringUtils.end_with(1, 2, 3, 4)


def test_negative_is_empty_none():
    with pytest.raises(TypeError):
        stringUtils.is_empty()


@pytest.mark.parametrize("string, res", [("", True), (" ", False)])
def test_negative_is_empty(string, res):
    text = stringUtils.is_empty(string)
    assert text == res


@pytest.mark.parametrize("string, res", [("Text", False),
                                         ("Text", False),
                                         ("1:2:3:4", False),
                                         ("23 августа", False),
                                         ("Это строка с пробелами", False)])
def test_positive_is_empty(string, res):
    text = stringUtils.is_empty(string)
    assert text == res


def test_is_empty():
    with pytest.raises(TypeError):
        stringUtils.is_empty(1, 2, 3, 4)


def test_negative_list_none():
    with pytest.raises(TypeError):
        stringUtils.list_to_string()


@pytest.mark.parametrize("my_list, res", [([], ""),
                                          ([], "")])
def test_negative_list_to_string(my_list, res):
    text = stringUtils.list_to_string(my_list)
    assert text == res


@pytest.mark.parametrize("my_list, joiner, res", [(["Text", "Test"], "/", "Text/Test"),
                                                  (["T", "e", "x", "t"], "", "Text"),
                                                  (["1", "2", "3", "4"], ":", "1:2:3:4"),
                                                  (["23", "августа", "1994"], " ", "23 августа 1994"),
                                                  (["Это", "строка", "с", "пробелами"],
                                                   "! ", "Это! строка! с! пробелами")])
def test_positive_list_to_string(my_list, joiner, res):
    text = stringUtils.list_to_string(my_list, joiner)
    assert text == res


def test_list_to_string():
    with pytest.raises(TypeError):
        stringUtils.list_to_string(1, 2, 3, 4)
