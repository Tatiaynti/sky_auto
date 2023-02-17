import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

def test_capitalize_word():
    stringUtils = StringUtils()
    res = stringUtils.capitilize('skypro')
    assert res == 'Skypro'

def test_capitalize_several_words():
    stringUtils = StringUtils()
    res = stringUtils.capitilize('skypro online')
    assert res == 'Skypro online'

def test_capitalize_letter():
    stringUtils = StringUtils()
    res = stringUtils.capitilize('s')
    assert res == 'S'

def test_trim_spaces_before_word():
    stringUtils = StringUtils()
    res = stringUtils.trim("   skypro")
    assert res == "skypro"

def test_trim_one_space():
    stringUtils = StringUtils()
    res = stringUtils.trim(" skypro")
    assert res == "skypro"

def test_trim_after_words():
    stringUtils = StringUtils()
    res = stringUtils.trim("skypro   ")
    assert res == "skypro   "

def test_trim_between_words():
    stringUtils = StringUtils()
    res = stringUtils.trim("sky  pro")
    assert res == "sky  pro"

def test_to_list_with_wrong_delimeter():
    stringUtils = StringUtils()
    res = stringUtils.to_list("a-b-c-d", "-")
    assert res == ["a", "b", "c", "d"] 

def test_to_list_with_other_delimeter():
    stringUtils = StringUtils()
    res = stringUtils.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]

def test_to_list_without_delimeter():
    stringUtils = StringUtils()
    res = stringUtils.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_to_list_empty():
    stringUtils = StringUtils()
    res = stringUtils.to_list("")
    assert res == []

def test_contains_true():
    stringUtils = StringUtils()
    res = stringUtils.contains("SkyPro", "S")
    assert res == True

def test_contains_false():
    stringUtils = StringUtils()
    res = stringUtils.contains("SkyPro", "U")
    assert res == False

def test_empty_contains():
    stringUtils = StringUtils()
    with pytest.raises(TypeError):
     stringUtils.contains("SkyPro")

def test_delete_symbol():
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol("SkyPro", "k")
    assert res == "SyPro"

def test_delete_symbols():
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol("SkyPro", "Pro")
    assert res == "Sky"

def test_delete_symbol_empty():
    stringUtils = StringUtils()
    with pytest.raises(TypeError):
     stringUtils.delete_symbol("SkyPro")

def test_delete_missing_symbol():
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol("SkyPro", "iy")
    assert res == "SkyPro"

def test_starts_with_true():
    stringUtils = StringUtils()
    res = stringUtils.starts_with("SkyPro", "S")
    assert res == True

def test_starts_with_false():
    stringUtils = StringUtils()
    res = stringUtils.starts_with("SkyPro", "P")
    assert res == False

def test_starts_with_empty():
    stringUtils = StringUtils()
    with pytest.raises(TypeError):
      stringUtils.starts_with("SkyPro")

def test_end_with_true():
    stringUtils = StringUtils()
    res = stringUtils.end_with("SkyPro", "o")
    assert res == True

def test_end_with_false():
    stringUtils = StringUtils()
    res = stringUtils.end_with("SkyPro", "y")
    assert res == False

def test_end_with_empty():
    stringUtils = StringUtils()
    with pytest.raises(TypeError):
      stringUtils.end_with("SkyPro")

def test_is_empty_no_spaces():
    stringUtils = StringUtils()
    res = stringUtils.is_empty("")
    assert res == True

def test_is_empty_one_space():
    stringUtils = StringUtils()
    res = stringUtils.is_empty(" ")
    assert res == True

def test_is_empty_one_word():
    stringUtils = StringUtils()
    res = stringUtils.is_empty("SkyPro")
    assert res == False

def test_is_empty_one_word():
    stringUtils = StringUtils()
    res = stringUtils.is_empty("SkyPro")
    assert res == False

def test_list_to_string_nums():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string([1,2,3,4])
    assert res == "1, 2, 3, 4"

def test_list_to_string_strings():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["Sky", "Pro"])
    assert res == "Sky, Pro"

def test_list_to_string_jointer():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["Sky", "Pro"], "-")
    assert res == "Sky-Pro"
